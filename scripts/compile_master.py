#!/usr/bin/env python3
"""
Step 1: Master Profile Compiler using Pandas.
Parses, validates, and transforms the section-agnostic master_table.tsv into:
  1. data/master_profile.json (Machine-readable SSOT for downstream tooling)
  2. data/master_profile.md   (Clean human-readable reference dossier)
"""

from pathlib import Path
import json
import re
import argparse
from collections import Counter
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TSV_PATH = REPO_ROOT / "data" / "master_table.tsv"
DEFAULT_JSON_PATH = REPO_ROOT / "data" / "master_profile.json"
DEFAULT_MD_PATH = REPO_ROOT / "data" / "master_profile.md"

REQUIRED_COLUMNS = [
    "id", "title", "description", "technologies",
    "start_date", "end_date", "organization",
    "engagement_type", "event_type", "target_archetypes",
    "confidence_level", "claim_type", "reference_url",
    "domain_tags", "impact"
]


def load_and_validate_table(table_path: Path) -> pd.DataFrame:
    if not table_path.exists():
        raise FileNotFoundError(f"Master table not found: {table_path}")

    sep = "\t" if table_path.suffix.lower() == ".tsv" else ","
    df = pd.read_csv(table_path, sep=sep, dtype=str).fillna("")

    # Strip whitespace across all string cells
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Validate required columns
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Table is missing required columns: {missing_cols}")

    # Validate ID uniqueness
    if not df["id"].is_unique:
        duplicates = df[df["id"].duplicated(keep=False)]["id"].tolist()
        raise ValueError(f"Duplicate IDs found in table: {set(duplicates)}")

    # Validate mandatory values
    empty_ids = df[df["id"] == ""]
    if not empty_ids.empty:
        raise ValueError("Found rows with empty 'id'")

    return df


def parse_delimited_field(val: str) -> list[str]:
    if not val:
        return []
    items = [item.strip() for item in val.split(";") if item.strip()]
    return items


def compile_json_data(df: pd.DataFrame) -> dict:
    entries = []
    skill_counter = Counter()
    skill_sources = {}
    domain_index = {}
    archetype_index = {}
    event_type_index = {}
    claim_type_index = {}
    confidence_index = {}

    for _, row in df.iterrows():
        tech_list = parse_delimited_field(row["technologies"])
        tags_list = parse_delimited_field(row["domain_tags"])
        archetypes_list = parse_delimited_field(row.get("target_archetypes", ""))
        ev_type = row.get("event_type", "Project")
        claim = row.get("claim_type", "Hands-on")
        conf = row.get("confidence_level", "High")

        for tech in tech_list:
            skill_counter[tech] += 1
            if tech not in skill_sources:
                skill_sources[tech] = []
            skill_sources[tech].append(row["id"])

        for tag in tags_list:
            clean_tag = tag.lower().replace("-", "_")
            if clean_tag not in domain_index:
                domain_index[clean_tag] = []
            domain_index[clean_tag].append(row["id"])

        for arch in archetypes_list:
            clean_arch = arch.lower().replace("-", "_")
            if clean_arch not in archetype_index:
                archetype_index[clean_arch] = []
            archetype_index[clean_arch].append(row["id"])

        if ev_type not in event_type_index:
            event_type_index[ev_type] = []
        event_type_index[ev_type].append(row["id"])

        if claim not in claim_type_index:
            claim_type_index[claim] = []
        claim_type_index[claim].append(row["id"])

        if conf not in confidence_index:
            confidence_index[conf] = []
        confidence_index[conf].append(row["id"])

        entry = {
            "id": row["id"],
            "title": row["title"],
            "description": row["description"],
            "technologies": tech_list,
            "start_date": row["start_date"],
            "end_date": row["end_date"],
            "period": f"{row['start_date']} - {row['end_date']}" if row['start_date'] != row['end_date'] else row['start_date'],
            "organization": row["organization"],
            "engagement_type": row["engagement_type"],
            "event_type": ev_type,
            "target_archetypes": archetypes_list,
            "confidence_level": conf,
            "claim_type": claim,
            "reference_url": row.get("reference_url", ""),
            "domain_tags": tags_list,
            "impact": row["impact"]
        }
        entries.append(entry)

    # Master skills inventory
    skills_inventory = [
        {
            "name": tech,
            "frequency": count,
            "associated_records": skill_sources[tech]
        }
        for tech, count in skill_counter.most_common()
    ]

    # 1. Candidate Contact & Basics (dynamically parsed from Profile entries in TSV)
    basics = {
        "name": "Poornachandra G.",
        "email": "poornachandra.gedi@gmail.com",
        "phone": "+91-7899 419758",
        "location": "Bengaluru, India",
        "linkedin": "https://www.linkedin.com/in/poornachandra-g-68045688/",
        "orcid": "https://orcid.org/0009-0009-1610-1205",
        "github": "https://github.com/bunnyboss",
        "portfolio": "https://bunnyboss.github.io/Portifolio/"
    }
    profile_df = df[df["id"].str.startswith("contact_") | (df["id"] == "basics_profile")]
    for _, row in profile_df.iterrows():
        key = row["id"].replace("contact_", "").replace("basics_", "")
        if row["description"]:
            basics[key] = row["description"]

    # 2. Summary Archetypes (dynamically parsed from Summary Archetype entries in TSV)
    summaries = {}
    summary_df = df[df["id"].str.startswith("summary_")]
    for _, row in summary_df.iterrows():
        key = row["id"].replace("summary_", "")
        summaries[key] = row["description"]

    # 3. Selected Highlights (dynamically parsed from Career Highlight entries in TSV)
    hl_df = df[df["id"].str.startswith("hl_")]
    selected_highlights = [
        f"{row['title']}: {row['description']}"
        for _, row in hl_df.iterrows()
    ]

    # 4. Skills Taxonomy (dynamically parsed from Skill Category entries in TSV)
    skills_taxonomy = {}
    skill_cat_df = df[df["id"].str.startswith("skill_cat_") | (df["event_type"] == "Skill Category")]
    for _, row in skill_cat_df.iterrows():
        cat_key = row["id"].replace("skill_cat_", "")
        tech_items = parse_delimited_field(row["technologies"])
        skills_taxonomy[cat_key] = tech_items

    # Extract Experience entries for Cellworks roles
    role_periods = [
        ("Lead Scientist Bioinformatics", "2024 - Present", "2024", "Present"),
        ("Senior Scientist, Reporting Manager", "2021 - 2024", "2021", "2024"),
        ("Senior Scientist, Bioinformatics", "2018 - 2021", "2018", "2021"),
        ("Scientist, Clinical Translation", "2017 - 2018", "2017", "2018"),
        ("Associate Scientist", "2015 - 2017", "2015", "2017")
    ]

    experience = []
    for role_name, period_str, s_yr, e_yr in role_periods:
        role_entries = [
            e for e in entries
            if e["organization"].startswith("Cellworks")
            and e["start_date"] == s_yr
            and e["end_date"] == e_yr
            and e["event_type"] != "Role"
            and not e["id"].startswith("cellworks_role_")
            and not e["id"].startswith("hl_")
        ]
        bullets = [e["description"] for e in role_entries]
        experience.append({
            "company": "Cellworks",
            "role": role_name,
            "period": period_str,
            "bullets": bullets,
            "record_ids": [e["id"] for e in role_entries]
        })

    # Extract Independent & Clinical AI projects
    project_entries = [
        e for e in entries
        if e["engagement_type"] in ["Independent", "Independent R&D"]
        and e.get("event_type", "Project") == "Project"
        and not e["id"].startswith("hl_")
    ]
    projects = []
    for p in project_entries:
        # Determine category based on tags
        cat = "Clinical & Bioinformatics AI"
        if "fullstack" in p["domain_tags"]:
            cat = "Full-Stack Applications"
        elif "developer_tools" in p["domain_tags"] or "finance" in p["domain_tags"]:
            cat = "Developer Tooling & Infrastructure"
        elif "agentic" in p["domain_tags"] or "mcp" in p["domain_tags"]:
            cat = "Agentic & LLM Tooling"

        projects.append({
            "id": p["id"],
            "name": p["title"].split(":")[0].strip(),
            "category": cat,
            "summary": p["description"],
            "tags": p["technologies"][:5],
            "impact": p["impact"]
        })

    # Publications
    pub_entries = [e for e in entries if "publication" in e["domain_tags"]]
    publications = [
        {
            "type": "Peer-Reviewed Journal" if "jco" in e["id"] or "gbm" in e["id"] else "Conference Abstract",
            "citation": e["description"],
            "year": e["start_date"],
            "journal": e["organization"]
        }
        for e in pub_entries
    ]

    # Education (dynamically parsed from Academic / education entries)
    edu_entries = [e for e in entries if e["engagement_type"] == "Academic" or "education" in e["domain_tags"]]
    education = [
        {
            "degree": e["title"],
            "institution": e["organization"],
            "year": e["end_date"],
            "location": "Andhra Pradesh, India",
            "description": e["description"]
        }
        for e in edu_entries
    ]

    # Honors & Awards (dynamically parsed from Honor / award entries)
    award_entries = [e for e in entries if e["id"].startswith("award_") or ("award" in e["domain_tags"] and e["engagement_type"] == "Honor")]
    honors_awards = [
        {
            "title": e["title"],
            "event": e["organization"],
            "year": e["end_date"],
            "description": e["description"]
        }
        for e in award_entries
    ]

    # Certifications & Workshops
    cert_entries = [e for e in entries if e["id"].startswith("cert_")]
    certifications_and_workshops = [
        {
            "title": e["title"],
            "organization": e["organization"],
            "type": e["engagement_type"]
        }
        for e in cert_entries
    ]

    master_data = {
        "basics": basics,
        "summaries": summaries,
        "selected_highlights": selected_highlights,
        "skills_taxonomy": skills_taxonomy,
        "experience": experience,
        "projects": projects,
        "education": education,
        "honors_awards": honors_awards,
        "publications": publications,
        "certifications_and_workshops": certifications_and_workshops,
        # Augmented Section-Agnostic Assets
        "section_agnostic_catalog": {
            "total_records": len(entries),
            "entries": entries,
            "skills_inventory": skills_inventory,
            "domain_index": domain_index,
            "archetype_index": archetype_index,
            "event_type_index": event_type_index,
            "claim_type_index": claim_type_index,
            "confidence_index": confidence_index
        }
    }

    return master_data


def compile_markdown_dossier(df: pd.DataFrame, master_data: dict) -> str:
    lines = [
        f"# {master_data['basics']['name']} — Master Career Dossier",
        f"**Lead Bioinformatics Scientist | Precision Medicine, Rare Diseases & Agentic AI Systems**",
        "",
        f"- **Email**: {master_data['basics']['email']}",
        f"- **Phone**: {master_data['basics']['phone']}",
        f"- **Location**: {master_data['basics']['location']}",
        f"- **LinkedIn**: [{master_data['basics']['linkedin']}]({master_data['basics']['linkedin']})",
        f"- **ORCID**: [{master_data['basics']['orcid']}]({master_data['basics']['orcid']})",
        f"- **GitHub**: [{master_data['basics']['github']}]({master_data['basics']['github']})",
        f"- **Portfolio**: [{master_data['basics']['portfolio']}]({master_data['basics']['portfolio']})",
        "",
        "---",
        "",
        "## 1. Professional Career Summaries by Archetype",
        ""
    ]

    archetype_titles = {
        "bioinformatics_lead": "Lead Bioinformatics Scientist / Clinical Genomics",
        "agentic_ai_engineer": "Agentic AI Engineer / LLMs & Multi-Agent Systems",
        "program_lead_ai": "Program Lead / AI Enablement & Delivery",
        "multi_omics_leader": "Bioinformatics & Multi-Omics Leader"
    }
    for key, title in archetype_titles.items():
        lines.append(f"### {title}")
        lines.append(master_data["summaries"].get(key, ""))
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 2. Selected Career Highlights & Quantified Impact",
        ""
    ])
    for hl in master_data["selected_highlights"]:
        lines.append(f"- {hl}")

    lines.extend([
        "",
        "---",
        "",
        "## 3. Career Timeline & Corporate Tenures (Cellworks)",
        ""
    ])

    for exp in master_data["experience"]:
        lines.append(f"### {exp['company']} — {exp['role']}")
        lines.append(f"*{exp['period']} | Bengaluru, India*")
        lines.append("")
        for b in exp["bullets"]:
            lines.append(f"- {b}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 4. Strategic Biopharma & Clinical Collaborations",
        ""
    ])

    collab_entries = [
        e for e in master_data["section_agnostic_catalog"]["entries"]
        if "collab_" in e["id"] or "/" in e["organization"] or e.get("engagement_type") == "Strategic Collaboration"
    ]
    for c in collab_entries:
        lines.append(f"### {c['title']} ({c['organization']})")
        lines.append(f"*{c['period']}*")
        lines.append(f"- **Description**: {c['description']}")
        lines.append(f"- **Technologies**: {', '.join(c['technologies'])}")
        lines.append(f"- **Impact**: {c['impact']}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 5. Independent AI & Clinical Engineering Innovations",
        ""
    ])

    for proj in master_data["projects"]:
        lines.append(f"### {proj['name']} ({proj['category']})")
        lines.append(f"- **Summary**: {proj['summary']}")
        lines.append(f"- **Technologies**: {', '.join(proj['tags'])}")
        lines.append(f"- **Impact**: {proj['impact']}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 6. Comprehensive Master Skills & Technologies Index",
        "Auto-compiled from historical records with frequency metrics:",
        ""
    ])

    for cat_name, skills in master_data["skills_taxonomy"].items():
        clean_title = cat_name.replace("_", " ").title()
        lines.append(f"- **{clean_title}**: {', '.join(skills)}")

    lines.extend([
        "",
        "---",
        "",
        "## 7. Honors, Awards & Academic Background",
        f"- **{master_data['honors_awards'][0]['title']} ({master_data['honors_awards'][0]['year']})**: {master_data['honors_awards'][0]['description']}",
        f"- **{master_data['education'][0]['degree']}** — {master_data['education'][0]['institution']} (*{master_data['education'][0]['year']}*)",
        "",
        "---",
        "",
        "## 8. Selected Peer-Reviewed Publications & Conference Abstracts",
        ""
    ])

    for pub in master_data["publications"]:
        lines.append(f"- {pub['citation']}")

    return "\n".join(lines)


def compile_master(table_path: Path = None, json_path: Path = None, md_path: Path = None) -> tuple[Path, Path]:
    table_p = table_path if table_path else DEFAULT_TSV_PATH
    json_p = json_path if json_path else DEFAULT_JSON_PATH
    md_p = md_path if md_path else DEFAULT_MD_PATH

    print(f"📊 Loading and validating master table: {table_p}")
    df = load_and_validate_table(table_p)
    print(f"✓ Table validated: {len(df)} records parsed with zero schema errors.")

    print("⚙️ Compiling JSON master profile data...")
    master_data = compile_json_data(df)

    json_p.parent.mkdir(parents=True, exist_ok=True)
    with open(json_p, "w", encoding="utf-8") as f:
        json.dump(master_data, f, indent=2)
    print(f"✓ JSON saved: {json_p} ({len(master_data['section_agnostic_catalog']['entries'])} catalog entries)")

    print("📝 Compiling Markdown career dossier...")
    md_content = compile_markdown_dossier(df, master_data)
    md_p.parent.mkdir(parents=True, exist_ok=True)
    with open(md_p, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✓ Markdown saved: {md_p}")

    return json_p, md_p


def main():
    parser = argparse.ArgumentParser(description="Compile section-agnostic Master Table into JSON & Markdown profiles.")
    parser.add_argument("--input", "-i", type=str, default=None, help="Path to input TSV/CSV table")
    parser.add_argument("--out-json", type=str, default=None, help="Path to output JSON file")
    parser.add_argument("--out-md", type=str, default=None, help="Path to output Markdown file")
    args = parser.parse_args()

    in_path = Path(args.input) if args.input else None
    out_json = Path(args.out_json) if args.out_json else None
    out_md = Path(args.out_md) if args.out_md else None

    compile_master(in_path, out_json, out_md)


if __name__ == "__main__":
    main()
