from schemas.base import BaseCompany

def normalize_pharma(sections: dict) -> BaseCompany:
    c = BaseCompany()
    c.sector = "Pharma"

    c.company_overview = sections.get("Business Description", "").strip()

    c.products_services = [
        line.replace("-", "").strip()
        for line in sections.get("Product & Services", "").splitlines()
        if line.strip()
    ]

    c.end_markets = sections.get(
        "Application areas / Industries served", ""
    ).split(",")

    c.market_size = sections.get("Market Size", "")
    c.revenue_trend = "Revenue growth driven by export markets and regulated geographies"
    c.margin_profile = "Margins supported by backward integration and scale efficiencies"

    c.investment_highlights = [
        "Regulatory-compliant manufacturing facilities",
        "Strong presence in export markets",
        "Diversified therapeutic portfolio",
        "High barriers to entry due to approvals and certifications"
    ]

    return c
