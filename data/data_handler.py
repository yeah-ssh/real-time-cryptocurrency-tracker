import requests
import json

def fetch_crypto_data():
    """Fetch cryptocurrency data from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,  
        'page': 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def fetch_portfolio():
    """Load portfolio data from a JSON file."""
    try:
        with open('data/portfolio.json', 'r') as f:
            portfolio = json.load(f)
    except FileNotFoundError:
        portfolio = {}
    return portfolio

def save_portfolio(portfolio):
    """Save the updated portfolio to a JSON file."""
    with open('data/portfolio.json', 'w') as f:
        json.dump(portfolio, f, indent=4)

def fetch_alerts():
    """Load alerts data from a JSON file."""
    try:
        with open('data/alerts.json', 'r') as f:
            alerts = json.load(f)
    except FileNotFoundError:
        alerts = {}
    return alerts

def save_alerts(alerts):
    """Save alerts to a JSON file."""
    with open('data/alerts.json', 'w') as f:
        json.dump(alerts, f, indent=4)
