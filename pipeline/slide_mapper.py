def map_slides(company):
    if company.sector == "Technology":
        return [
            ("Company Overview", company.company_overview),
            ("Technology & Capabilities", "\n".join(company.products_services)),
            ("Growth & Investment Highlights", "\n".join(company.investment_highlights))
        ]

    if company.sector == "Logistics":
        return [
            ("Network & Operations", company.company_overview),
            ("Service Differentiation", "\n".join(company.products_services)),
            ("Strategic Highlights", "\n".join(company.investment_highlights))
        ]
