from schemas.base import BaseCompany

def normalize_consumer(sections: dict) -> BaseCompany:
    c = BaseCompany()
    c.sector = "Consumer"

    c.company_overview = sections.get("Business Description", "").strip()

    c.products_services = [
        line.replace("-", "").strip()
        for line in sections.get("Product & Services", "").splitlines()
        if line.strip()
    ]

    c.end_markets = ["Direct-to-Consumer", "Online Marketplaces"]

    c.market_size = sections.get("Market Size", "")
    c.revenue_trend = "High-growth trajectory driven by brand adoption"
    c.margin_profile = "Strong gross margins supported by direct sales channels"

    c.investment_highlights = [
        "Strong brand recall in core categories",
        "Asset-light operating model",
        "High repeat customer rate",
        "Large whitespace opportunity in branded consumption"
    ]

    return c
