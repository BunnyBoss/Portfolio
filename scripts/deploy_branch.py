#!/usr/bin/env python3
"""
Step 4: Branch-based Vercel Portfolio Deployment Tool
Creates a dedicated Git branch per application, customizes docs/index.html and resume download links,
and optionally pushes to GitHub to trigger an automatic Vercel preview deployment.
"""

import re
import subprocess
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", text).strip("-")


def run_git_cmd(cmd: list[str]) -> str:
    res = subprocess.run(cmd, cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Git command failed: {' '.join(cmd)}\nError: {res.stderr.strip()}")
    return res.stdout.strip()


def customize_portfolio_html(company: str, role: str) -> Path:
    company_slug = slugify(company)
    html_path = REPO_ROOT / "docs" / "index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title
    content = re.sub(
        r"<title>.*?</title>",
        f"<title>Poornachandra G. | {role} @ {company}</title>",
        content,
        count=1
    )

    # 2. Update Typing Text / Subtitle
    content = re.sub(
        r'<span class="typing-text">.*?</span>',
        f'<span class="typing-text">{role}</span>',
        content,
        count=1
    )

    # 3. Update Hero Badge text
    content = re.sub(
        r'<span class="badge-text">.*?</span>',
        f'<span class="badge-text">Targeted for {company}</span>',
        content,
        count=1
    )

    # 4. Update Resume Download Link
    pdf_filename = f"{company_slug}_resume.pdf"
    # Ensure PDF link points to the tailored document
    content = re.sub(
        r'href="assets/documents/.*?"\s+class="btn btn-primary btn-block"\s+download=".*?"',
        f'href="assets/documents/{pdf_filename}" class="btn btn-primary btn-block" download="Poornachandra_G_{company_slug}_Resume.pdf"',
        content,
        count=1
    )

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✓ Customized docs/index.html for {company} ({role})")
    return html_path


def deploy_branch(company: str, role: str, push: bool = False, remote: str = "origin") -> str:
    company_slug = slugify(company)
    role_slug = slugify(role)
    branch_name = f"apply/{company_slug}-{role_slug}"

    print(f"🚀 Preparing application branch: {branch_name}")

    # 1. Customize HTML
    customize_portfolio_html(company, role)

    # 2. Check if branch exists
    branches = run_git_cmd(["git", "branch", "--list", branch_name])
    if branches:
        print(f"Switching to existing branch {branch_name}...")
        run_git_cmd(["git", "checkout", branch_name])
    else:
        print(f"Creating and switching to new branch {branch_name}...")
        run_git_cmd(["git", "checkout", "-b", branch_name])

    # 3. Add modified files
    files_to_stage = [
        ".gitignore",
        "docs/index.html",
        "vercel.json",
        f"docs/assets/documents/{company_slug}_resume.pdf",
        f"assets/documents/{company_slug}_resume.pdf",
        f"applications/{company_slug}-{role_slug}/"
    ]
    for pattern in files_to_stage:
        path = REPO_ROOT / pattern
        if path.exists():
            run_git_cmd(["git", "add", "-f", pattern])

    # 4. Commit
    commit_msg = (
        f"feat(portfolio): customize resume & portfolio for {company} - {role}\n\n"
        f"Co-Authored-By: Claude Code <noreply@anthropic.com>"
    )
    status = run_git_cmd(["git", "status", "--porcelain"])
    if status:
        run_git_cmd(["git", "commit", "-m", commit_msg])
        print(f"✓ Committed changes to {branch_name}")
    else:
        print("No changes to commit (already up to date).")

    # 5. Push if requested
    if push:
        print(f"Pushing {branch_name} to {remote}...")
        try:
            run_git_cmd(["git", "push", "-u", remote, branch_name])
            print(f"✓ Successfully pushed {branch_name} to {remote}")
        except Exception as e:
            print(f"⚠️ Push failed or remote not configured: {e}")
            print(f"You can manually push using: git push -u {remote} {branch_name}")

    # Generate Vercel preview link format
    vercel_subdomain = f"portfolio-git-apply-{company_slug}-{role_slug}-bunnyboss.vercel.app"
    print("\n🌐 Vercel Preview Deployment Info:")
    print(f"  • Branch: {branch_name}")
    print(f"  • Expected Preview URL: https://{vercel_subdomain}")
    print("  • Note: Every push to this branch triggers an isolated preview deployment on Vercel.")

    return branch_name


def main():
    parser = argparse.ArgumentParser(description="Create tailored portfolio branch for Vercel deployment.")
    parser.add_argument("--company", required=True, help="Target company name")
    parser.add_argument("--role", required=True, help="Target role title")
    parser.add_argument("--push", action="store_true", help="Push branch to remote repository")
    parser.add_argument("--remote", default="origin", help="Git remote name (default: origin)")

    args = parser.parse_args()
    deploy_branch(args.company, args.role, push=args.push, remote=args.remote)


if __name__ == "__main__":
    main()
