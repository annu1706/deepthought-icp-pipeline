import pandas as pd
from playwright.sync_api import sync_playwright
import json
import time

companies = pd.read_csv("data/companies.csv")

results = []

def scrape_website(url):
    pages_to_try = [
        "",
        "/about",
        "/about-us",
        "/products",
        "/leadership"
    ]

    full_text = ""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for path in pages_to_try:
            try:
                page.goto(url + path, timeout=10000)

                text = page.locator("body").inner_text()

                full_text += text[:3000]

                time.sleep(1)

            except:
                continue

        browser.close()

    return full_text


for index, row in companies.iterrows():

    print(f"Scraping: {row['company_name']}")

    text = scrape_website(row['website'])

    results.append({
        "company": row['company_name'],
        "website": row['website'],
        "content": text
    })

with open("output/scraped_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Done scraping.")