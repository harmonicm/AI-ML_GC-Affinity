def detect_sector(sections, company_slug=None):
    """
    Robust sector detection using:
    1. Company slug (primary)
    2. MD content (secondary)
    """

    if company_slug:
        slug = company_slug.lower()

        if "tech" in slug or "ksolves" in slug:
            return "technology"
        if "logistics" in slug or "gati" in slug:
            return "logistics"
        if "pharma" in slug or "swift" in slug:
            return "pharma"
        if "electronics" in slug or "centum" in slug:
            return "electronics"
        if "automotive" in slug or "kalyani" in slug:
            return "automotive"
        if "entertainment" in slug or "connplex" in slug:
            return "consumer"

    # -------- Fallback: content-based ----------
    text = " ".join(sections.values()).lower()

    if "software" in text or "saas" in text or "it services" in text:
        return "technology"
    if "logistics" in text or "transport" in text or "warehouse" in text:
        return "logistics"
    if "pharma" in text or "formulation" in text or "api" in text:
        return "pharma"
    if "automotive" in text or "forging" in text:
        return "automotive"
    if "electronics" in text or "pcb" in text:
        return "electronics"

    return "general"
