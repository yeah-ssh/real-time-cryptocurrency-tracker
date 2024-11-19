import requests
from config import API_URL

def fetch_crypto_data():
    url = f"{API_URL}/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10}
    response = requests.get(url, params=params)
    return response.json()
