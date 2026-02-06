from schemas.base import BaseCompany

def normalize_manufacturing(sections: dict) -> BaseCompany:
    c = BaseCompany()
    c.sector = "Manufacturing"

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
    c.revenue_trend = "Stable revenue growth supported by long-term OEM relationships"
    c.margin_profile = "Attractive margins driven by scale and process efficiencies"

    c.investment_highlights = [
        "Diversified product portfolio with high entry barriers",
        "Long-standing relationships with marquee customers",
        "Multi-location manufacturing footprint",
        "Strong compliance and certification base"
    ]

    return c
