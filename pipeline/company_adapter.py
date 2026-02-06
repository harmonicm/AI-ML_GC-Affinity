class PPTCompany:
    def __init__(self, base):
        self.name = getattr(base, "company_name", "Company X")

        self.business_description = getattr(
            base, "business_description", ""
        )

        self.products = getattr(
            base, "products_services", []
        )

        # ---------- FIXED MARKET SIZE NORMALIZATION ----------
        raw_market = getattr(base, "market_size", [])

        self.market_size = []
        for m in raw_market:
            if isinstance(m, dict):
                self.market_size.append({
                    "market": m.get("market", "Market"),
                    "growth": m.get("growth", 0)
                })
            elif isinstance(m, str):
                # fallback when only market name exists
                self.market_size.append({
                    "market": m,
                    "growth": 1   # dummy value so pie chart renders
                })

        # ---------- FINANCIALS ----------
        self.financials = {
            "revenue": getattr(base, "revenue", "N/A"),
            "pat": getattr(base, "pat", "N/A"),
            "ebitda": getattr(base, "ebitda", "N/A"),
        }

        self.swot = getattr(
            base, "swot", {
                "strengths": [],
                "opportunities": []
            }
        )

        self.future_plan = getattr(
            base, "future_plan", []
        )
