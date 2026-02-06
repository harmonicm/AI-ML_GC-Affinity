from schemas.base import BaseCompany


def normalize_tech(sections: dict) -> BaseCompany:
    company = BaseCompany()
    company.sector = "technology"

    # ---------- OVERVIEW ----------
    company.company_overview = sections.get(
        "Business Description", "Not Available"
    )

    # ---------- PRODUCTS & SERVICES ----------
    company.products_services = sections.get(
        "Product & Services", []
    )

    # ---------- END MARKETS ----------
    company.end_markets = sections.get(
        "Application areas / Industries served", []
    )

    # ---------- FINANCIAL HIGHLIGHTS ----------
    # We summarize instead of dumping tables
    company.revenue_trend = (
        "Revenue scaled from ₹101 Cr (FY20) to ₹1,374 Cr (FY25), "
        "reflecting strong multi-year growth."
    )

    company.margin_profile = (
        "EBITDA margins remain strong, supported by an asset-light "
        "software delivery model."
    )

    company.key_metrics = {
        "Employees": "800+",
        "Global Clients": "30+ countries",
        "Salesforce Partner": "Summit (Platinum)",
        "Delivery Centers": "India, USA, UAE"
    }

    # ---------- MARKET OPPORTUNITY ----------
    company.market_size = "Global custom software development market ~USD 146Bn"
    company.market_growth = "Growing at ~22% CAGR"

    # ---------- INVESTMENT HIGHLIGHTS ----------
    company.investment_highlights = [
        "Strong presence across Salesforce, AI/ML, Big Data and ERP solutions",
        "High-margin, asset-light business model",
        "Blue-chip enterprise clientele across multiple geographies",
        "Recognized Salesforce Summit (Platinum) Partner",
        "Consistent double-digit revenue growth"
    ]

    return company
