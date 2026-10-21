#!/usr/bin/env python3
"""
Step 3: Refine Final Tailored Resume for Given JD
Reads JD analysis & master profile to generate custom ATS-compliant Markdown and WeasyPrint PDF.
"""

import json
import re
import argparse
from pathlib import Path
from generate_pdf import generate_pdf

REPO_ROOT = Path(__file__).resolve().parent.parent
MASTER_PROFILE_PATH = REPO_ROOT / "data" / "master_profile.json"


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", text).strip("-")


def tailor_resume(company: str, role: str, analysis_path: Path = None) -> tuple[Path, Path]:
    company_slug = slugify(company)
    role_slug = slugify(role)
    app_dir = REPO_ROOT / "applications" / f"{company_slug}-{role_slug}"
    app_dir.mkdir(parents=True, exist_ok=True)

    if analysis_path is None:
        analysis_path = app_dir / "jd_analysis.json"

    # Load master profile
    with open(MASTER_PROFILE_PATH, "r", encoding="utf-8") as f:
        profile = json.load(f)

    # Load analysis if available
    analysis = None
    if analysis_path.exists():
        with open(analysis_path, "r", encoding="utf-8") as f:
            analysis = json.load(f)

    archetype_key = analysis["archetype"]["key"] if analysis else "bioinformatics_lead"

    # If role combines both Bioinformatics and AI (e.g. Amgen Bioinformatics & AI Engineer)
    role_lower = role.lower()
    if ("bioinformatics" in role_lower or "computational biology" in role_lower) and ("ai" in role_lower or "ml" in role_lower or "machine learning" in role_lower):
        if "bioinformatics_ai_engineer" in profile["summaries"]:
            archetype_key = "bioinformatics_ai_engineer"

    # Sourced strictly from master_table.tsv via master_profile.json
    summary_text = profile["summaries"].get(archetype_key, profile["summaries"]["bioinformatics_lead"])

    # Determine role title display
    role_display = f"{role} | Precision Medicine & Agentic AI Systems"

    # Select and prioritize skills
    matched_cats = analysis.get("matched_skills_by_category", {}) if analysis else {}
    ordered_skills = []

    # Map categories to clean labels
    label_map = {
        "ngs_clinical_omics": "Applied Bioinformatics & Clinical-omics",
        "pipeline_engineering": "Pipeline Engineering",
        "machine_learning_ai": "Machine Learning & AI",
        "llms_agentic_systems": "LLMs & Agentic Systems",
        "programming_engineering": "Programming & Engineering",
        "cloud_infrastructure": "Cloud, Platforms & Infrastructure",
        "nlp_ocr_document_ai": "NLP, OCR & Document AI",
        "visualization_ui": "Visualization & UI",
        "leadership_delivery": "Leadership & Delivery"
    }

    # Prioritize matched categories first, then remainder
    all_categories = list(profile["skills_taxonomy"].keys())
    prioritized_cats = sorted(all_categories, key=lambda c: len(matched_cats.get(c, [])), reverse=True)

    for cat in prioritized_cats:
        skills = profile["skills_taxonomy"][cat]
        if cat in matched_cats and matched_cats[cat]:
            # Put matched skills first in line
            matched = matched_cats[cat]
            others = [s for s in skills if s not in matched]
            combined = matched + others
        else:
            combined = skills
        label = label_map.get(cat, cat.replace("_", " ").title())
        ordered_skills.append((label, " • ".join(combined)))

    # Curate projects
    selected_projects = []
    if analysis and analysis.get("top_recommended_projects"):
        selected_projects = analysis["top_recommended_projects"][:3]
    else:
        # Default top projects
        selected_projects = profile["projects"][:3]

    # Build Markdown
    contact_line = (
        f"✉ <a href=\"mailto:{profile['basics']['email']}\">{profile['basics']['email']}</a> • "
        f"☎ {profile['basics']['phone']} • "
        f"📍 {profile['basics']['location']} • "
        f"<a href=\"{profile['basics']['linkedin']}\">LinkedIn</a> • "
        f"<a href=\"{profile['basics']['orcid']}\">ORCID</a> • "
        f"<a href=\"{profile['basics']['portfolio']}\">Portfolio</a>"
    )

    lines = [
        f"# {profile['basics']['name']}",
        f"**{role_display}**",
        "",
        contact_line,
        "",
        "## PROFESSIONAL SUMMARY",
        summary_text,
        "",
        "## SELECTED HIGHLIGHTS & IMPACT"
    ]

    for h in profile["selected_highlights"]:
        lines.append(f"- {h}")

    lines.extend([
        "",
        "## SKILLS & TECHNOLOGIES"
    ])
    for label, skills_str in ordered_skills:
        lines.append(f"- **{label}:** {skills_str}")

    lines.extend([
        "",
        "## PROFESSIONAL EXPERIENCE",
        ""
    ])

    for exp in profile["experience"]:
        lines.append(f"**{exp['company']} - {exp['role']}** | *{exp['period']}*")
        for b in exp["bullets"]:
            lines.append(f"- {b}")
        lines.append("")

    lines.extend([
        "## KEY PROJECTS & INNOVATIONS",
        ""
    ])
    for proj in selected_projects:
        tags_str = " • ".join(proj.get("tags", []))
        lines.append(f"**{proj['name']}** ({proj.get('category', 'AI')}) | *{tags_str}*")
        lines.append(f"- {proj['summary']}")
        lines.append("")

    lines.extend([
        "## EDUCATION",
        f"**{profile['education'][0]['degree']}** — {profile['education'][0]['institution']} (*{profile['education'][0]['year']}*)",
        "",
        "## HONORS & AWARDS",
        f"- **{profile['honors_awards'][0]['title']} ({profile['honors_awards'][0]['year']})**: {profile['honors_awards'][0]['description']}",
        "",
        "## SELECTED PUBLICATIONS",
    ])

    for pub in profile["publications"][:5]:
        lines.append(f"- {pub['citation']}")

    md_content = "\n".join(lines)
    resume_md_path = app_dir / "resume.md"
    with open(resume_md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    # Generate PDF
    resume_pdf_path = app_dir / "resume.pdf"
    doc_resume_pdf = REPO_ROOT / "docs" / "assets" / "documents" / f"{company_slug}_resume.pdf"
    asset_resume_pdf = REPO_ROOT / "assets" / "documents" / f"{company_slug}_resume.pdf"

    generate_pdf(
        input_md_path=resume_md_path,
        output_pdf_paths=[resume_pdf_path, doc_resume_pdf, asset_resume_pdf]
    )

    print(f"✓ Tailored resume generated successfully:")
    print(f"  • Markdown: {resume_md_path}")
    print(f"  • PDF: {resume_pdf_path}")
    print(f"  • Portfolio Document: {doc_resume_pdf}")

    return resume_md_path, resume_pdf_path


def main():
    parser = argparse.ArgumentParser(description="Tailor resume for target company and role.")
    parser.add_argument("--company", required=True, help="Target company name")
    parser.add_argument("--role", required=True, help="Target role title")
    parser.add_argument("--analysis", default=None, help="Path to jd_analysis.json (optional)")

    args = parser.parse_args()
    analysis_p = Path(args.analysis) if args.analysis else None
    tailor_resume(args.company, args.role, analysis_p)


if __name__ == "__main__":
    main()
