from schemas.tech import normalize_tech
from schemas.logistics import normalize_logistics
from schemas.pharma import normalize_pharma
from schemas.manufacturing import normalize_manufacturing


def normalize_company(sector, sections):
    if sector == "technology":
        return normalize_tech(sections)
    elif sector == "logistics":
        return normalize_logistics(sections)
    elif sector == "pharma":
        return normalize_pharma(sections)
    elif sector == "manufacturing":
        return normalize_manufacturing(sections)
    else:
        raise ValueError(f"Unsupported sector: {sector}")

