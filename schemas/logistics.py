from schemas.base import BaseCompany

def normalize_logistics(sections: dict) -> BaseCompany:
    c = BaseCompany()
    c.sector = "Logistics"

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
    c.revenue_trend = "Revenue growth supported by network expansion and service diversification"
    c.margin_profile = "Improving EBITDA margins driven by operational efficiency"

    c.investment_highlights = [
        "Pan-India express logistics network",
        "Technology-enabled tracking and fulfillment",
        "Strong ESG and sustainability initiatives",
        "Exposure to high-growth e-commerce and retail segments"
    ]

    return c
