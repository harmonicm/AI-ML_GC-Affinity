from pathlib import Path

DATA_DIR = Path("Company Data")

def load_company_md(company_slug: str) -> str:
    """
    company_slug examples:
    - logistics-gati
    - technology-ksolves
    """

    folder = DATA_DIR / company_slug

    if not folder.exists():
        raise FileNotFoundError(
            f"Company folder not found: {folder.resolve()}"
        )

    md_files = list(folder.glob("*.md"))

    if len(md_files) == 0:
        raise FileNotFoundError("No .md file found in company folder")

    if len(md_files) > 1:
        raise ValueError("Expected exactly one .md file per company folder")

    return md_files[0].read_text(encoding="utf-8")
