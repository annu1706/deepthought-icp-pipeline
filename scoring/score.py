import json
import pandas as pd
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

# Gemini client setup
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Load scraped company data
with open("output/scraped_data.json", "r", encoding="utf-8") as f:
    companies = json.load(f)

results = []

# Loop through companies
for company in companies:

    print(f"Scoring: {company['company']}")

    prompt = f"""
    Analyze this manufacturing company.

    Give scores from 1-10 for:

    C1: Manufacturer
    C2: Revenue Fit
    C3: Product Differentiation
    C4: Technical Leadership
    C5: Export/Regulatory Signals
    C6: Growth Signals

    Also give:
    - Final Verdict (PASS or FAIL)
    - Short reason

    Return ONLY valid JSON.

    Company Content:
    {company['content'][:2000]}
    """

    try:

        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        output = response.choices[0].message.content

        results.append({
            "company": company["company"],
            "result": output
        })

        print(f"Done: {company['company']}")

        # Avoid rate limit
        time.sleep(10)

    except Exception as e:

        print(f"Error for {company['company']}: {e}")

        results.append({
            "company": company["company"],
            "result": f"ERROR: {e}"
        })

# Save final results
df = pd.DataFrame(results)

df.to_csv("output/final_scores.csv", index=False)

print("Scoring complete.")