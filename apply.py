#!/usr/bin/env python3
"""
Job Application Engine: Single Source of Truth & Application Automation
Executes the 4-step job application workflow:
  1. Master Repository: data/master_profile.json
  2. JD Analysis: scripts/analyze_jd.py
  3. Resume Tailoring: scripts/tailor_resume.py
  4. Vercel Branch Portfolio Deployment: scripts/deploy_branch.py
"""

import sys
import argparse
from pathlib import Path

# Add scripts directory to path
REPO_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from analyze_jd import analyze_jd, save_analysis, slugify
from tailor_resume import tailor_resume
from deploy_branch import deploy_branch
from compile_master import compile_master


def cmd_compile(args):
    print(f"\n[Step 1] Compiling Master Profile from tabular SSOT...")
    in_path = Path(args.input) if hasattr(args, "input") and args.input else None
    json_path, md_path = compile_master(in_path)
    print(f"✓ Master Profile compiled successfully:")
    print(f"  • JSON: {json_path}")
    print(f"  • Markdown: {md_path}")
    return json_path, md_path


def cmd_analyze(args):
    print(f"\n[Step 2] Analyzing Job Description for {args.company} ({args.role})...")
    analysis = analyze_jd(args.company, args.role, args.jd)
    company_slug = slugify(args.company)
    role_slug = slugify(args.role)
    output_dir = REPO_ROOT / "applications" / f"{company_slug}-{role_slug}"
    json_path, md_path = save_analysis(analysis, output_dir)
    print(f"✓ Analysis complete:")
    print(f"  • Match Score: {analysis['match_metrics']['estimated_match_score']}")
    print(f"  • Detected Archetype: {analysis['archetype']['name']}")
    print(f"  • JSON Report: {json_path}")
    print(f"  • Markdown Report: {md_path}")
    return json_path


def cmd_tailor(args):
    print(f"\n[Step 3] Tailoring resume for {args.company} ({args.role})...")
    md_path, pdf_path = tailor_resume(args.company, args.role)
    print(f"✓ Tailored resume ready:")
    print(f"  • Markdown: {md_path}")
    print(f"  • PDF: {pdf_path}")
    return md_path, pdf_path


def cmd_branch(args):
    print(f"\n[Step 4] Deploying portfolio branch for {args.company} ({args.role})...")
    branch = deploy_branch(args.company, args.role, push=args.push, remote=args.remote)
    print(f"✓ Branch {branch} successfully prepared and customized.")
    return branch


def cmd_all(args):
    print(f"\n=======================================================")
    print(f"🚀 Running End-to-End Application Workflow for {args.company}")
    print(f"Role: {args.role}")
    print(f"=======================================================")

    # Step 1: Compile Master Profile from TSV
    cmd_compile(args)

    # Step 2: Analyze JD
    cmd_analyze(args)

    # Step 3: Tailor Resume (Markdown + PDF)
    cmd_tailor(args)

    # Step 4: Branch and Prepare Portfolio for Vercel
    cmd_branch(args)

    print("\n🎉 All 4 steps successfully completed!")


def main():
    parser = argparse.ArgumentParser(
        description="Unified Job Application Engine (Master Data, JD Analysis, Resume Tailoring, Branch Deploy)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python apply.py compile
  python apply.py all --company "Genentech" --role "Lead Bioinformatics Scientist" --jd path/to/jd.txt --push
  python apply.py analyze --company "Anthropic" --role "AI Systems Engineer" --jd path/to/jd.txt
  python apply.py tailor --company "Anthropic" --role "AI Systems Engineer"
  python apply.py branch --company "Anthropic" --role "AI Systems Engineer" --push
        """
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: compile (Step 1)
    p_compile = subparsers.add_parser("compile", help="Compile master_table.tsv into master_profile.json & master_profile.md")
    p_compile.add_argument("--input", "-i", default=None, help="Path to input TSV/CSV table (default: data/master_table.tsv)")

    # Subcommand: analyze
    p_analyze = subparsers.add_parser("analyze", help="Decompose JD and extract match/gap analysis")
    p_analyze.add_argument("--company", required=True, help="Target company name")
    p_analyze.add_argument("--role", required=True, help="Target role title")
    p_analyze.add_argument("--jd", required=True, help="Path to JD file or raw text string")

    # Subcommand: tailor
    p_tailor = subparsers.add_parser("tailor", help="Generate tailored Markdown & PDF resume")
    p_tailor.add_argument("--company", required=True, help="Target company name")
    p_tailor.add_argument("--role", required=True, help="Target role title")

    # Subcommand: branch
    p_branch = subparsers.add_parser("branch", help="Create Git branch with customized portfolio for Vercel")
    p_branch.add_argument("--company", required=True, help="Target company name")
    p_branch.add_argument("--role", required=True, help="Target role title")
    p_branch.add_argument("--push", action="store_true", help="Push to git remote (triggers Vercel preview)")
    p_branch.add_argument("--remote", default="origin", help="Git remote name (default: origin)")

    # Subcommand: all
    p_all = subparsers.add_parser("all", help="Execute all 4 steps end-to-end")
    p_all.add_argument("--company", required=True, help="Target company name")
    p_all.add_argument("--role", required=True, help="Target role title")
    p_all.add_argument("--jd", required=True, help="Path to JD file or raw text string")
    p_all.add_argument("--push", action="store_true", help="Push to git remote (triggers Vercel preview)")
    p_all.add_argument("--remote", default="origin", help="Git remote name (default: origin)")

    args = parser.parse_args()

    if args.command == "compile":
        cmd_compile(args)
    elif args.command == "analyze":
        cmd_analyze(args)
    elif args.command == "tailor":
        cmd_tailor(args)
    elif args.command == "branch":
        cmd_branch(args)
    elif args.command == "all":
        cmd_all(args)


if __name__ == "__main__":
    main()
