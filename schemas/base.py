class BaseCompany:
    def __init__(self):
        # -------- Identity --------
        self.sector = ""   # technology / pharma / logistics / etc.

        # -------- Slide 1: Business Overview --------
        self.overview = ""                 # rewritten 3–4 line paragraph
        self.business_model = ""           # optional short line
        self.products_services = []        # list[str]
        self.end_markets = []              # list[str]

        # -------- Slide 2: Scale & Financials --------
        self.key_metrics = []              # list[str] (presentation-ready)

        self.financials = {                # presentation-ready
            "revenue": "",
            "margin": "",
            "profitability": ""
        }

        self.market = {                    # structured for charts
            "size": "",                    # e.g. "$150Bn"
            "growth": "",                  # e.g. "15% CAGR"
            "segments": []                 # optional
        }

        # -------- Slide 3: Investment Highlights --------
        self.investment_highlights = []    # list[str]

        # -------- Metadata (future use) --------
        self.sources = {}                  # {field: source}

