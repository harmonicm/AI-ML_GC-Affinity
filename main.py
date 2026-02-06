import sys
from pipeline.loader import load_company_md
from pipeline.md_parser import parse_markdown_sections
from pipeline.sector_classifier import detect_sector
from pipeline.ppt_generator import generate_ppt_from_sections


def run(company_slug):
    md_text = load_company_md(company_slug)
    sections = parse_markdown_sections(md_text)

    sector = detect_sector(sections, company_slug)


    generate_ppt_from_sections(
        sections,
        f"output/{company_slug}.pptx",
        sector=sector
    )

    print(f"[✔] Generated PPT for {company_slug} ({sector})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <company-slug>")
        sys.exit(1)

    run(sys.argv[1])
