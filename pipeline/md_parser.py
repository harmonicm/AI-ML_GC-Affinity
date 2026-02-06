import re

def parse_markdown_sections(md_text: str) -> dict:
    sections = {}
    current_section = None
    buffer = []

    for line in md_text.splitlines():
        header_match = re.match(r"^##\s+(.*)", line)
        if header_match:
            if current_section:
                sections[current_section] = "\n".join(buffer).strip()
            current_section = header_match.group(1).strip()
            buffer = []
        else:
            buffer.append(line)

    if current_section:
        sections[current_section] = "\n".join(buffer).strip()

    return sections
