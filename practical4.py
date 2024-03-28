import requests
import sys
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY=os.getenv("API_KEY")
SEARCH_ENGINE_ID= os.getenv('SEARCH_ENGINE_ID')
# API_KEY = "AIzaSyDiLuEait44hgVJqzvYMaxrrra0-GNfxKo"
# SEARCH_ENGINE_ID = "5782c3b64d30b471e"

try:
    query = input('Enter your query : ')
except:
    print("Please specify a search query")
    exit()

start = 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
data = requests.get(url).json()
search_items = data.get("items")
try:
    for i, search_item in enumerate(search_items, start=1):
        try:
            long_description = search_item["pagemap"]["metatags"][0]["og:description"]
        except KeyError:
            long_description = "N/A"
        title = search_item.get("title")
        snippet = search_item.get("snippet")
        html_snippet = search_item.get("htmlSnippet")
        link = search_item.get("link")
        print("="*10, f"Result #{i+start-1}", "="*10)
        print("Title:", title)
        print("Description:", snippet)
        print("Long description:", long_description)
        print("URL:", link, "\n")
except Exception as e:
    print('N/A')