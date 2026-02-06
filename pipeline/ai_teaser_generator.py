from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a senior M&A investment banker.

Given company information, generate a 3-slide BLIND investment teaser
as per Kelp M&A guidelines.

Rules:
- Do NOT mention company name
- Rewrite text anonymously
- Adapt content to sector
- Be concise, professional, investor-ready
- Output STRICT JSON ONLY
"""

def generate_teaser(sector: str, sections: dict):

    user_prompt = f"""
Sector: {sector}

Company Data:
{json.dumps(sections, indent=2)}

Generate a 3-slide blind investment teaser.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        print("[WARN] OpenAI unavailable, using fallback teaser")

        return {
            "slides": [
                {
                    "title": "Business Overview",
                    "bullets": [
                        f"Sector-focused company operating in the {sector} space",
                        "Established operating model with diversified offerings",
                        "Serves enterprise and institutional customers"
                    ],
                    "chart": None,
                    "image_query": None
                },
                {
                    "title": "Scale & Market Opportunity",
                    "bullets": [
                        "Operates in a large and growing addressable market",
                        "Favorable industry growth drivers",
                        "Scalable platform with expansion potential"
                    ],
                    "chart": None,
                    "image_query": None
                },
                {
                    "title": "Investment Highlights",
                    "bullets": [
                        "Strong competitive positioning",
                        "Experienced management team",
                        "Attractive long-term growth outlook"
                    ],
                    "chart": None,
                    "image_query": None
                }
            ],
            "citations": []
        }


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    return json.loads(response.choices[0].message.content)

