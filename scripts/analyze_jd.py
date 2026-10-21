#!/usr/bin/env python3
"""
Step 2: JD & Company Analysis Tool
Decomposes Job Descriptions, analyzes company context, and maps requirements against master profile.
"""

import json
import re
import argparse
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parent.parent
MASTER_PROFILE_PATH = REPO_ROOT / "data" / "master_profile.json"


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", text).strip("-")


def load_master_profile() -> dict:
    with open(MASTER_PROFILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def read_jd_content(jd_input: str) -> str:
    if len(jd_input) < 1000:
        try:
            path = Path(jd_input)
            if path.is_file():
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    return f.read()
        except OSError:
            pass
    return jd_input


def classify_archetype(role_title: str, jd_text: str) -> tuple[str, str]:
    text = f"{role_title} {jd_text}".lower()

    scores = {
        "bioinformatics_lead": 0,
        "agentic_ai_engineer": 0,
        "program_lead_ai": 0,
        "multi_omics_leader": 0,
    }

    # Archetype signal words
    bioinfo_signals = ["bioinformatics", "ngs", "variant", "clinical genomics", "gatk", "wes", "wgs", "rna-seq", "acmg", "wes", "pipeline", "nextflow"]
    ai_signals = ["agent", "multi-agent", "langchain", "langgraph", "llm", "rag", "eval", "prompt", "promptfoo", "deepeval", "agentic", "genai", "mcp"]
    program_signals = ["program lead", "program manager", "agile", "scrum", "stakeholder", "delivery", "enablement", "roadmapping", "pmo", "operations"]
    multi_omics_signals = ["multi-omics", "biomarker", "target discovery", "crispr", "depmap", "pharmacogenomics", "translational", "biomedical data"]

    for word in bioinfo_signals:
        scores["bioinformatics_lead"] += len(re.findall(rf"\b{re.escape(word)}\b", text))
    for word in ai_signals:
        scores["agentic_ai_engineer"] += len(re.findall(rf"\b{re.escape(word)}\b", text))
    for word in program_signals:
        scores["program_lead_ai"] += len(re.findall(rf"\b{re.escape(word)}\b", text))
    for word in multi_omics_signals:
        scores["multi_omics_leader"] += len(re.findall(rf"\b{re.escape(word)}\b", text))

    top_archetype = max(scores, key=scores.get)
    # Default fallback if text is sparse
    if scores[top_archetype] == 0:
        top_archetype = "bioinformatics_lead"

    display_names = {
        "bioinformatics_lead": "Lead Bioinformatics Scientist / Clinical Genomics",
        "agentic_ai_engineer": "Agentic AI Engineer / LLMs & Multi-Agent Systems",
        "program_lead_ai": "Program Lead / AI Enablement & Delivery",
        "multi_omics_leader": "Bioinformatics & Multi-Omics Leader"
    }

    return top_archetype, display_names[top_archetype]


def extract_matched_skills(jd_text: str, profile: dict) -> dict:
    jd_lower = jd_text.lower()
    matched_skills = {}
    missing_skills = []
    all_known_skills = []

    for category, skill_list in profile["skills_taxonomy"].items():
        matched_category = []
        for skill in skill_list:
            all_known_skills.append(skill)
            # Normalize check: exact word boundary or substring for acronyms
            pattern = rf"(?i)\b{re.escape(skill)}\b"
            if re.search(pattern, jd_lower):
                matched_category.append(skill)
        if matched_category:
            matched_skills[category] = matched_category

    # Check common tech keywords in JD that might not be in master profile
    common_industry_keywords = [
        "Docker", "Kubernetes", "Nextflow", "Snakemake", "AWS", "GCP", "Azure",
        "Terraform", "FastAPI", "GraphQL", "PostgreSQL", "Snowflake", "BigQuery",
        "PyTorch", "TensorFlow", "Scikit-Learn", "LangChain", "LlamaIndex",
        "CrewAI", "AutoGen", "vLLM", "Triton", "CUDA", "C++", "Java", "Go", "Rust"
    ]
    for kw in common_industry_keywords:
        if re.search(rf"(?i)\b{re.escape(kw)}\b", jd_lower):
            # Check if this keyword is already represented
            is_represented = any(kw.lower() in s.lower() for s in all_known_skills)
            if not is_represented and kw not in missing_skills:
                missing_skills.append(kw)

    return {
        "matched": matched_skills,
        "potential_gaps": missing_skills
    }


def rank_relevant_projects(jd_text: str, profile: dict) -> list[dict]:
    jd_lower = jd_text.lower()
    ranked = []

    for proj in profile.get("projects", []):
        score = 0
        reasons = []

        # Tag matches
        for tag in proj.get("tags", []):
            if re.search(rf"(?i)\b{re.escape(tag)}\b", jd_lower):
                score += 3
                reasons.append(f"Tag matched: {tag}")

        # Summary/Impact matches
        tokens = re.findall(r"\b[A-Za-z]{4,}\b", proj.get("summary", "") + " " + proj.get("impact", ""))
        for token in set(tokens):
            if re.search(rf"(?i)\b{re.escape(token)}\b", jd_lower):
                score += 1

        if score > 0:
            ranked.append({
                "id": proj["id"],
                "name": proj["name"],
                "category": proj["category"],
                "score": score,
                "reasons": reasons[:3],
                "summary": proj["summary"],
                "tags": proj["tags"]
            })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


def analyze_jd(company: str, role: str, jd_input: str) -> dict:
    profile = load_master_profile()
    jd_text = read_jd_content(jd_input)

    archetype_key, archetype_name = classify_archetype(role, jd_text)
    skills_analysis = extract_matched_skills(jd_text, profile)
    ranked_projects = rank_relevant_projects(jd_text, profile)

    # Calculate match metric
    total_matched_skills = sum(len(v) for v in skills_analysis["matched"].values())
    match_score = min(98, max(55, total_matched_skills * 4 + (len(ranked_projects) * 3)))

    analysis = {
        "target": {
            "company": company,
            "role": role,
            "company_slug": slugify(company),
            "role_slug": slugify(role),
        },
        "archetype": {
            "key": archetype_key,
            "name": archetype_name,
            "recommended_summary": profile["summaries"].get(archetype_key, profile["summaries"]["bioinformatics_lead"])
        },
        "match_metrics": {
            "estimated_match_score": f"{match_score}%",
            "matched_skills_count": total_matched_skills,
            "matched_projects_count": len(ranked_projects)
        },
        "matched_skills_by_category": skills_analysis["matched"],
        "potential_gaps_or_bonus_terms": skills_analysis["potential_gaps"],
        "top_recommended_projects": ranked_projects[:4],
        "talking_points": [
            f"Tailored for {company}'s {role} opening with focus on {archetype_name}.",
            f"Emphasize 10+ years of clinical & production bioinformatics and modern AI engineering.",
            f"Leverage relevant hands-on projects: {', '.join([p['name'] for p in ranked_projects[:3]]) if ranked_projects else 'VarEffex, PathoParse, SQL Chat'}."
        ]
    }

    return analysis


def save_analysis(analysis: dict, output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "jd_analysis.json"
    md_path = output_dir / "jd_analysis.md"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(analysis, f, indent=2)

    # Build Markdown report
    lines = [
        f"# Job Description & Company Analysis: {analysis['target']['company']} — {analysis['target']['role']}",
        "",
        f"**Estimated Match Score**: `{analysis['match_metrics']['estimated_match_score']}`  ",
        f"**Role Archetype Detected**: **{analysis['archetype']['name']}**  ",
        f"**Recommended Summary Profile**: `{analysis['archetype']['key']}`  ",
        "",
        "---",
        "",
        "## 1. Company & Role Alignment Strategy",
        f"Targeting **{analysis['target']['company']}** for the role of **{analysis['target']['role']}**.",
        "",
        "### Key Talking Points & Pitch Angle:",
    ]
    for pt in analysis["talking_points"]:
        lines.append(f"- {pt}")

    lines.extend([
        "",
        "---",
        "",
        "## 2. Matched Skills Taxonomy",
        "The following skills from your Master Profile directly align with this role:"
    ])

    for cat, skills in analysis["matched_skills_by_category"].items():
        clean_cat = cat.replace("_", " ").title()
        lines.append(f"- **{clean_cat}**: {', '.join(skills)}")

    if analysis["potential_gaps_or_bonus_terms"]:
        lines.extend([
            "",
            "### Bonus Terms / Potential Gaps in JD:",
            f"Terms mentioned in JD to address during interviews or in customized bullets: `{', '.join(analysis['potential_gaps_or_bonus_terms'])}`"
        ])

    lines.extend([
        "",
        "---",
        "",
        "## 3. Top Recommended Projects to Showcase"
    ])

    for proj in analysis["top_recommended_projects"]:
        lines.append(f"### {proj['name']} ({proj['category']})")
        lines.append(f"- **Summary**: {proj['summary']}")
        lines.append(f"- **Tags**: {', '.join(proj['tags'])}")
        lines.append("")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return json_path, md_path


def main():
    parser = argparse.ArgumentParser(description="Decompose JD and match against Master Profile.")
    parser.add_argument("--company", required=True, help="Target company name")
    parser.add_argument("--role", required=True, help="Target role title")
    parser.add_argument("--jd", required=True, help="Path to JD file or raw text string")
    parser.add_argument("--outdir", default=None, help="Custom output directory")

    args = parser.parse_args()

    analysis = analyze_jd(args.company, args.role, args.jd)

    company_slug = analysis["target"]["company_slug"]
    role_slug = analysis["target"]["role_slug"]
    output_dir = Path(args.outdir) if args.outdir else REPO_ROOT / "applications" / f"{company_slug}-{role_slug}"

    json_path, md_path = save_analysis(analysis, output_dir)
    print(f"✓ Analysis complete for {args.company} ({args.role}):")
    print(f"  • JSON: {json_path}")
    print(f"  • Markdown: {md_path}")
    print(f"  • Match Score: {analysis['match_metrics']['estimated_match_score']}")
    print(f"  • Archetype: {analysis['archetype']['name']}")


if __name__ == "__main__":
    main()
