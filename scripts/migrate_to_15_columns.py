#!/usr/bin/env python3
"""
Migrates data/master_table.tsv to the enhanced 15-column schema:
1. id
2. title
3. description
4. technologies
5. start_date
6. end_date
7. organization
8. engagement_type   (Corporate | Independent | Academic | Professional Body | Profile)
9. event_type         (Role | Project | Responsibility | Certification | Course / Workshop | Publication | Award | Degree | Profile Meta)
10. target_archetypes (bioinformatics; agentic_ai; program_management; multi_omics)
11. confidence_level  (High | Medium | Low)
12. claim_type        (Hands-on | Augmented | ATS Insertion)
13. reference_url     (Web link, repo URL, DOI, or empty)
14. domain_tags       (Query tags)
15. impact            (Quantifiable outcome / XYZ metric)
"""

from pathlib import Path
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
TSV_PATH = REPO_ROOT / "data" / "master_table.tsv"
BACKUP_PATH = REPO_ROOT / "data" / "master_table_backup_10col.tsv"

def determine_metadata(row):
    row_id = row["id"]
    eng_orig = row["engagement_type"]
    tags = row["domain_tags"]
    org = row["organization"]
    title = row["title"]

    # 1. Defaults
    engagement = eng_orig
    event_type = "Project"
    archetypes = ["bioinformatics"]
    confidence = "High"
    claim = "Hands-on"
    url = ""

    # 2. Profile & Metadata
    if eng_orig == "Profile" or row_id.startswith("contact_"):
        engagement = "Profile"
        event_type = "Profile Meta"
        archetypes = ["bioinformatics", "agentic_ai", "program_management", "multi_omics"]
        confidence = "High"
        claim = "Hands-on"
        if "linkedin" in row_id:
            url = row["description"]
        elif "orcid" in row_id:
            url = row["description"]
        elif "github" in row_id:
            url = row["description"]
        elif "portfolio" in row_id:
            url = row["description"]

    elif eng_orig == "Summary Archetype" or row_id.startswith("summary_"):
        engagement = "Profile"
        event_type = "Profile Meta"
        confidence = "High"
        claim = "Hands-on"
        if "bioinformatics" in row_id:
            archetypes = ["bioinformatics", "clinical"]
        elif "agentic" in row_id:
            archetypes = ["agentic_ai"]
        elif "program" in row_id:
            archetypes = ["program_management"]
        elif "multi_omics" in row_id:
            archetypes = ["multi_omics", "bioinformatics"]

    elif eng_orig == "Career Highlight" or row_id.startswith("hl_"):
        engagement = "Corporate" if org == "Cellworks" else "Independent"
        event_type = "Responsibility" if "leadership" in tags or "mentorship" in tags or "hiring" in tags else "Project"
        confidence = "High"
        claim = "Augmented"
        if "bioinformatics" in tags:
            archetypes.append("bioinformatics")
        if "ai" in tags or "llm" in tags:
            archetypes.append("agentic_ai")
        if "leadership" in tags or "management" in tags:
            archetypes.append("program_management")
        if "multi_omics" in tags:
            archetypes.append("multi_omics")

    # 3. Academic
    elif eng_orig == "Academic" or row_id.startswith("edu_"):
        engagement = "Academic"
        event_type = "Degree"
        archetypes = ["bioinformatics", "multi_omics"]
        confidence = "High"
        claim = "Hands-on"

    # 4. Awards
    elif row_id.startswith("award_"):
        engagement = "Independent"
        event_type = "Award"
        archetypes = ["bioinformatics", "multi_omics"]
        confidence = "High"
        claim = "Hands-on"
        url = "https://bunnyboss.github.io/Portifolio/"

    # 5. Certifications & Workshops
    elif row_id.startswith("cert_"):
        engagement = "Professional Body"
        if "workshop" in title.lower() or "optimization" in title.lower():
            event_type = "Course / Workshop"
        else:
            event_type = "Certification"
        confidence = "High"
        claim = "Hands-on"
        if "aws" in row_id:
            archetypes = ["bioinformatics", "program_management"]
        elif "acmg" in row_id:
            archetypes = ["bioinformatics", "clinical"]
        elif "ai" in row_id:
            archetypes = ["agentic_ai", "program_management"]
        elif "dragen" in row_id:
            archetypes = ["bioinformatics"]

    # 6. Publications
    elif row_id.startswith("pub_") or "publication" in tags:
        engagement = "Corporate"
        event_type = "Publication"
        archetypes = ["bioinformatics", "multi_omics"]
        confidence = "High"
        claim = "Hands-on"
        url = "https://orcid.org/0009-0009-1610-1205"

    # 7. Strategic Collaborations (absorb into Corporate)
    elif eng_orig == "Strategic Collaboration" or "collab_" in row_id:
        engagement = "Corporate"
        event_type = "Project"
        archetypes = ["bioinformatics", "multi_omics"]
        confidence = "High"
        claim = "Hands-on"

    # 8. Independent R&D Projects
    elif eng_orig == "Independent R&D" or row_id.startswith("proj_"):
        engagement = "Independent"
        event_type = "Project"
        confidence = "High"
        claim = "Hands-on"
        url = f"https://github.com/bunnyboss/{row_id.replace('proj_', '')}"
        if "rare_disease" in row_id or "pathoparse" in row_id or "vareffex" in row_id:
            archetypes = ["bioinformatics", "agentic_ai"]
        elif "fullstack" in tags or "developer_tools" in tags or "finance" in tags:
            archetypes = ["agentic_ai", "fullstack"]
        else:
            archetypes = ["agentic_ai"]

    # 9. Corporate (Cellworks)
    elif eng_orig == "Corporate" or org == "Cellworks":
        engagement = "Corporate"
        # Determine if Responsibility or Project
        if any(w in tags for w in ["leadership", "management", "hiring", "mentoring", "risk_management", "compliance"]):
            event_type = "Responsibility"
            archetypes = ["program_management", "bioinformatics"]
        else:
            event_type = "Project"
            if "ai" in tags or "multi_agent" in tags or "prompt_engineering" in tags:
                archetypes = ["agentic_ai", "bioinformatics"]
            elif "multi_omics" in tags:
                archetypes = ["multi_omics", "bioinformatics"]
            else:
                archetypes = ["bioinformatics"]

    # Deduplicate and sort archetypes
    clean_archetypes = sorted(list(set(archetypes)))
    archetypes_str = "; ".join(clean_archetypes)

    return engagement, event_type, archetypes_str, confidence, claim, url

def main():
    print(f"Reading {TSV_PATH}...")
    df = pd.read_csv(TSV_PATH, sep="\t", dtype=str).fillna("")
    print(f"Loaded {len(df)} records.")

    # Save backup
    df.to_csv(BACKUP_PATH, sep="\t", index=False)
    print(f"Saved 10-column backup to {BACKUP_PATH}")

    new_rows = []
    for _, row in df.iterrows():
        eng, ev_type, archs, conf, claim, url = determine_metadata(row)
        new_row = {
            "id": row["id"],
            "title": row["title"],
            "description": row["description"],
            "technologies": row["technologies"],
            "start_date": row["start_date"],
            "end_date": row["end_date"],
            "organization": row["organization"],
            "engagement_type": eng,
            "event_type": ev_type,
            "target_archetypes": archs,
            "confidence_level": conf,
            "claim_type": claim,
            "reference_url": url,
            "domain_tags": row["domain_tags"],
            "impact": row["impact"]
        }
        new_rows.append(new_row)

    # Add explicit Role entries for Cellworks 5 tenures
    cellworks_roles = [
        {
            "id": "cellworks_role_lead_bioinformatician",
            "title": "Lead Bioinformatician & R&D Team Lead",
            "description": "Leading the Bioinformatics R&D team: defining technical roadmaps, recruiting and mentoring scientists, driving project prioritization, and delivering clinical-grade multi-omics and AI-driven solutions.",
            "technologies": "Technical Roadmapping; Team Leadership; Agile; Scrum; Nextflow; GATK; Multi-Agent Systems; JIRA",
            "start_date": "2024",
            "end_date": "Present",
            "organization": "Cellworks",
            "engagement_type": "Corporate",
            "event_type": "Role",
            "target_archetypes": "bioinformatics; program_management",
            "confidence_level": "High",
            "claim_type": "Hands-on",
            "reference_url": "https://www.linkedin.com/in/poornachandra-g-68045688/",
            "domain_tags": "leadership; role; management; roadmap; hiring; bioinformatics",
            "impact": "Led bioinformatics team, delivered 100% of pipeline milestones on schedule"
        },
        {
            "id": "cellworks_role_senior_scientist_reporting",
            "title": "Senior Scientist, Reporting Manager",
            "description": "Led a team of 4 scientists; developed production pipelines for clinical biomarker estimation (MSI, HRD, TMB); architected high-throughput variant calling on AWS Batch; harmonized multi-vendor genomic inputs.",
            "technologies": "AWS Batch; Nextflow; Python; Docker; MSI; HRD; TMB; GATK; Variant Calling; Mentoring",
            "start_date": "2021",
            "end_date": "2024",
            "organization": "Cellworks",
            "engagement_type": "Corporate",
            "event_type": "Role",
            "target_archetypes": "bioinformatics; program_management",
            "confidence_level": "High",
            "claim_type": "Hands-on",
            "reference_url": "https://www.linkedin.com/in/poornachandra-g-68045688/",
            "domain_tags": "leadership; role; management; aws; cloud; biomarkers; clinical",
            "impact": "Managed 4 direct reports, scaled AWS pipeline throughput by 3x"
        },
        {
            "id": "cellworks_role_senior_scientist_bioinformatics",
            "title": "Senior Scientist, Bioinformatics",
            "description": "Benchmarked secondary analysis pipelines (DRAGEN, Parabricks, Sentieon) cutting turnaround time by 40%; designed liquid-biopsy panels; built tumor-only Panel of Normals (PoN) workflows.",
            "technologies": "DRAGEN; NVIDIA Parabricks; Sentieon; Liquid Biopsy; Panel Design; GATK; Python; Bash; PoN",
            "start_date": "2018",
            "end_date": "2021",
            "organization": "Cellworks",
            "engagement_type": "Corporate",
            "event_type": "Role",
            "target_archetypes": "bioinformatics; multi_omics",
            "confidence_level": "High",
            "claim_type": "Hands-on",
            "reference_url": "https://www.linkedin.com/in/poornachandra-g-68045688/",
            "domain_tags": "bioinformatics; role; benchmarking; secondary_analysis; liquid_biopsy; ngs",
            "impact": "40% reduction in secondary analysis turnaround time"
        },
        {
            "id": "cellworks_role_scientist_clinical_translation",
            "title": "Scientist, Clinical Translation",
            "description": "Curated therapy rationale libraries; analyzed 200+ complex cancer cases; benchmarked clinical sequencing pipelines; built in-house variant annotation and tier-filtering tools.",
            "technologies": "VEP; ANNOVAR; Variant Annotation; Clinical Oncology; Python; Shell; Tier Filtering",
            "start_date": "2017",
            "end_date": "2018",
            "organization": "Cellworks",
            "engagement_type": "Corporate",
            "event_type": "Role",
            "target_archetypes": "bioinformatics; clinical",
            "confidence_level": "High",
            "claim_type": "Hands-on",
            "reference_url": "https://www.linkedin.com/in/poornachandra-g-68045688/",
            "domain_tags": "bioinformatics; role; clinical; oncology; variant_interpretation; tier_filtering",
            "impact": "Curated 200+ cancer patient genomics profiles with actionable therapy rationales"
        },
        {
            "id": "cellworks_role_associate_scientist",
            "title": "Associate Scientist",
            "description": "Harmonized multi-omics data for >500 cases; automated ETL pipelines for TCGA & GDSC cohorts; established report generation templating engine.",
            "technologies": "Python; Shell; TCGA; GDSC; Multi-Omics; ETL; Automated Reporting; Data Curation",
            "start_date": "2015",
            "end_date": "2017",
            "organization": "Cellworks",
            "engagement_type": "Corporate",
            "event_type": "Role",
            "target_archetypes": "bioinformatics; multi_omics",
            "confidence_level": "High",
            "claim_type": "Hands-on",
            "reference_url": "https://www.linkedin.com/in/poornachandra-g-68045688/",
            "domain_tags": "bioinformatics; role; multi_omics; etl; tcga; gdsc; automation",
            "impact": "Harmonized >500 clinical multi-omics profiles and automated reporting workflow"
        }
    ]

    new_rows.extend(cellworks_roles)

    new_df = pd.DataFrame(new_rows)
    # Ensure exact 15 column order
    cols_order = [
        "id", "title", "description", "technologies",
        "start_date", "end_date", "organization",
        "engagement_type", "event_type", "target_archetypes",
        "confidence_level", "claim_type", "reference_url",
        "domain_tags", "impact"
    ]
    new_df = new_df[cols_order]

    new_df.to_csv(TSV_PATH, sep="\t", index=False)
    print(f"✓ Migration complete: {len(new_df)} rows written to {TSV_PATH} with 15 columns.")

if __name__ == "__main__":
    main()
