import requests
import pandas as pd

API_KEY = ""

unique_items_url = "https://www.pathofexile.com/api/trade/data/items"
divination_cards_url = "https://www.pathofexile.com/api/trade/data/divination-cards"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(unique_items_url, headers=headers)
data = response.json()

unique_items = [
    {"id": item["id"], "name": item["name"]}
    for item in data["result"]
]

for item in unique_items:
    response = requests.get(
        divination_cards_url,
        headers=headers,
        params={"type": item["name"]}
    )
    data = response.json()

divination_cards = [
    {"id": card["id"], "name": card["name"]}
    for card in data["result"]
]
item["divination_cards"] = divination_cards

df = pd.DataFrame(unique_items)
df.to_csv("unique_items.csv", index=False)

