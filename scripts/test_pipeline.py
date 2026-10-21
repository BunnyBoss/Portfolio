#!/usr/bin/env python3
"""
Runnable self-check for the 4-step Job Application Toolkit.
Tests master profile loading, JD analysis, resume tailoring, PDF generation, and portfolio customization.
"""

import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from analyze_jd import analyze_jd, save_analysis, load_master_profile
from tailor_resume import tailor_resume
from deploy_branch import customize_portfolio_html


def test_master_profile():
    profile = load_master_profile()
    assert "basics" in profile, "Missing 'basics' in master profile"
    assert "summaries" in profile, "Missing 'summaries' in master profile"
    assert "skills_taxonomy" in profile, "Missing 'skills_taxonomy' in master profile"
    assert "experience" in profile and len(profile["experience"]) >= 4, "Missing experience entries"
    assert "projects" in profile and len(profile["projects"]) >= 3, "Missing projects entries"
    assert "publications" in profile and len(profile["publications"]) >= 5, "Missing publications"
    assert "education" in profile, "Missing education"
    print("✓ Step 1 Check: Master profile is valid and complete.")


def test_jd_analysis():
    sample_jd = """
    We are hiring a Lead AI Systems Engineer at BioGen.
    Requirements:
    - 5+ years experience building LLMs, RAG pipelines, and multi-agent workflows using LangChain or LangGraph.
    - Strong Python, FastAPI, and Nextflow knowledge.
    - Clinical-omics or variant interpretation understanding is a huge plus.
    - Experience with prompt evaluation (Promptfoo, DeepEval) and observability.
    """
    analysis = analyze_jd("BioGen", "Lead AI Systems Engineer", sample_jd)
    assert analysis["archetype"]["key"] == "agentic_ai_engineer", f"Wrong archetype: {analysis['archetype']['key']}"
    assert "llms_agentic_systems" in analysis["matched_skills_by_category"], "Failed to match LLM skills"
    assert len(analysis["top_recommended_projects"]) >= 1, "Failed to rank projects"

    out_dir = REPO_ROOT / "applications" / "test-company-test-role"
    json_path, md_path = save_analysis(analysis, out_dir)
    assert json_path.exists(), "JSON analysis not written"
    assert md_path.exists(), "Markdown analysis not written"
    print("✓ Step 2 Check: JD analysis successfully decomposed and saved.")


def test_resume_tailoring():
    md_path, pdf_path = tailor_resume("BioGen", "Lead AI Systems Engineer")
    assert md_path.exists(), "resume.md was not generated"
    assert pdf_path.exists(), "resume.pdf was not generated"
    assert pdf_path.stat().st_size > 10000, "Generated PDF is suspiciously small"
    print("✓ Step 3 Check: Tailored resume Markdown and PDF generated successfully.")


def test_portfolio_customization():
    html_path = customize_portfolio_html("BioGen", "Lead AI Systems Engineer")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Lead AI Systems Engineer" in content, "HTML subtitle not updated"
    assert "BioGen" in content, "HTML company tag not updated"
    assert "biogen_resume.pdf" in content, "Resume link not updated to target PDF"
    print("✓ Step 4 Check: Portfolio HTML customization works as expected.")


def main():
    print("Running 4-Step Job Application Toolkit Self-Checks...\n")
    test_master_profile()
    test_jd_analysis()
    test_resume_tailoring()
    test_portfolio_customization()
    print("\n🎉 ALL CHECKS PASSED: 4-step pipeline is fully operational!")


if __name__ == "__main__":
    main()
