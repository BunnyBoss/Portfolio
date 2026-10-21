#!/usr/bin/env python3
"""
PDF Generation Utility using Markdown, BeautifulSoup, and WeasyPrint.
Supports custom input and output paths via CLI or programmatic import.
"""

from pathlib import Path
import markdown
from bs4 import BeautifulSoup
import argparse
from weasyprint import HTML

REPO_ROOT = Path(__file__).resolve().parent.parent


def generate_pdf(input_md_path: Path = None, output_pdf_paths: list[Path] = None):
    if input_md_path is None:
        input_md_path = REPO_ROOT / 'applied_bioinformatics_resume.md'
    else:
        input_md_path = Path(input_md_path)

    if not input_md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {input_md_path}")

    # 1. Read Markdown
    with open(input_md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 2. Convert to HTML
    html_content = markdown.markdown(text, extensions=['extra', 'sane_lists'])

    # 3. Process with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # CSS Styles
    css_content = """
    @page {
        size: A4;
        margin: 10mm 13mm 11mm 13mm;
        @bottom-right {
            content: counter(page) " / " counter(pages);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            font-size: 8pt;
            color: #888;
        }
    }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        color: #2c3e50;
        font-size: 9.2pt;
        line-height: 1.34;
        margin: 0;
        padding: 0;
    }
    h1 {
        color: #1a4971;
        text-align: center;
        font-size: 20pt;
        font-weight: 700;
        letter-spacing: 0.3px;
        margin-bottom: 3px;
        margin-top: 0;
    }
    .role-title {
        text-align: center;
        font-size: 11pt;
        font-weight: 600;
        color: #216093;
        margin-bottom: 4px;
    }
    .contact-info {
        text-align: center;
        font-size: 8.8pt;
        color: #4b5563;
        margin-bottom: 11px;
    }
    .contact-info a {
        color: #216093;
        text-decoration: none;
    }
    h2 {
        color: #1a4971;
        border-bottom: 1.5px solid #1a4971;
        padding-bottom: 2px;
        font-size: 11pt;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin-top: 10px;
        margin-bottom: 4px;
        page-break-after: avoid;
        break-after: avoid;
    }
    /* Skills Table */
    .skills-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 8px;
        page-break-inside: auto;
    }
    .skills-table tr {
        page-break-inside: avoid;
        break-inside: avoid;
    }
    .skills-table td {
        border: 1px solid #e2e8f0;
        padding: 3px 6px;
        font-size: 8.8pt;
        line-height: 1.3;
        vertical-align: top;
    }
    .skills-table td:first-child {
        color: #1a4971;
        font-weight: 600;
        width: 25%;
        background-color: #f8fafc;
    }
    .experience-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-top: 7px;
        margin-bottom: 2px;
        page-break-after: avoid;
        break-after: avoid;
        page-break-inside: avoid;
        break-inside: avoid;
    }
    .experience-header strong {
        font-size: 10pt;
        color: #0f172a;
    }
    .experience-header em {
        font-size: 9pt;
        color: #64748b;
        font-style: normal;
    }
    ul {
        margin-top: 2px;
        padding-left: 17px;
        margin-bottom: 5px;
    }
    li {
        margin-bottom: 2px;
        font-size: 9pt;
        line-height: 1.32;
        page-break-inside: avoid;
        break-inside: avoid;
    }
    p {
        margin-top: 0;
        margin-bottom: 6px;
        font-size: 9pt;
        line-height: 1.34;
    }
    a {
        color: #216093;
        text-decoration: none;
    }
    @media screen {
        body {
            background-color: #f1f5f9;
            padding: 25px 15px;
            display: flex;
            justify-content: center;
        }
        .resume-container {
            max-width: 820px;
            width: 100%;
            background: #ffffff;
            padding: 38px 45px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border-radius: 4px;
            box-sizing: border-box;
        }
    }
    @media print {
        body {
            background: transparent;
            padding: 0;
        }
        .resume-container {
            max-width: none;
            padding: 0;
            box-shadow: none;
            border-radius: 0;
        }
    }
    """

    # Transform header section
    h1 = soup.find('h1')
    if h1:
        role_p = h1.find_next_sibling('p')
        if role_p:
            contact_p = role_p.find_next_sibling('p')
            if contact_p and ('@' in contact_p.get_text() or 'mailto' in str(contact_p) or 'LinkedIn' in contact_p.get_text()):
                # Create a container div for header
                header_container = soup.new_tag('div')

                # Create a div for role title
                role_div = soup.new_tag('div')
                role_div['class'] = 'role-title'
                role_div.append(BeautifulSoup(role_p.decode_contents(), 'html.parser'))

                # Create a div for contact info
                contact_div = soup.new_tag('div')
                contact_div['class'] = 'contact-info'
                contact_div.append(BeautifulSoup(contact_p.decode_contents(), 'html.parser'))

                header_container.append(role_div)
                header_container.append(contact_div)

                role_p.replace_with(header_container)
                contact_p.decompose()

    # Transform skills list into a table
    h2_skills = soup.find(lambda tag: tag.name == "h2" and "SKILLS" in tag.text.upper())
    if h2_skills:
        ul_skills = h2_skills.find_next_sibling('ul')
        if ul_skills:
            table = soup.new_tag('table')
            table['class'] = 'skills-table'

            for li in ul_skills.find_all('li'):
                strong = li.find('strong')
                if strong:
                    cat_name = strong.get_text().strip(': ')
                    strong.extract()
                    details = li.get_text().strip(': \n\t')

                    tr = soup.new_tag('tr')
                    td1 = soup.new_tag('td')
                    td1.string = cat_name
                    td2 = soup.new_tag('td')
                    td2.string = details

                    tr.append(td1)
                    tr.append(td2)
                    table.append(tr)

            ul_skills.replace_with(table)

    # Transform Experience Header
    for p in soup.find_all('p'):
        strong = p.find('strong')
        em = p.find('em')
        if strong and em and '|' in p.get_text():
            text_lines = p.get_text().split('\n')

            div = soup.new_tag('div')
            div['class'] = 'experience-header'

            strong_tag = soup.new_tag('strong')
            strong_tag.string = strong.get_text()

            em_tag = soup.new_tag('em')
            em_tag.string = em.get_text()

            div.append(strong_tag)
            div.append(em_tag)

            ul_tag = soup.new_tag('ul')
            for line in text_lines[1:]:
                if line.strip().startswith('-'):
                    li = soup.new_tag('li')
                    li.string = line.strip()[1:].strip()
                    ul_tag.append(li)
                elif line.strip():
                    if len(ul_tag.contents) > 0:
                        ul_tag.contents[-1].string += " " + line.strip()
                    else:
                        li = soup.new_tag('li')
                        li.string = line.strip()
                        ul_tag.append(li)

            new_container = soup.new_tag('div')
            new_container.append(div)
            if len(ul_tag.contents) > 0:
                new_container.append(ul_tag)

            p.replace_with(new_container)

    # Wrap it all in standard HTML
    final_html = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
        {css_content}
        </style>
    </head>
    <body>
        <div class="resume-container">
            {str(soup)}
        </div>
    </body>
    </html>
    """

    # 4. Generate PDF outputs
    if not output_pdf_paths:
        output_pdf_assets = REPO_ROOT / 'assets' / 'documents' / 'applied_bioinformatics_resume.pdf'
        output_pdf_docs = REPO_ROOT / 'docs' / 'assets' / 'documents' / 'applied_bioinformatics_resume.pdf'
        output_pdf_paths = [output_pdf_assets, output_pdf_docs]

    rendered = HTML(string=final_html, base_url=str(REPO_ROOT))
    for path in output_pdf_paths:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        # Save HTML preview alongside PDF for browser inspection
        html_path = path.with_suffix('.html')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        rendered.write_pdf(str(path))
        print(f"✓ PDF generated: {path}")
        print(f"✓ HTML preview generated: {html_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate PDF resume from Markdown")
    parser.add_argument("--input", "-i", type=str, default=None, help="Input markdown file path")
    parser.add_argument("--output", "-o", action="append", help="Output PDF file path(s)")
    args = parser.parse_args()

    in_path = Path(args.input) if args.input else None
    out_paths = [Path(p) for p in args.output] if args.output else None
    generate_pdf(in_path, out_paths)


if __name__ == '__main__':
    main()
