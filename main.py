import requests
import time
from data.gainers_losers import get_top_gainers_and_losers
from data.currency_converter import convert_currency
from data.price_alerts import set_price_alert
from data.market_overview import display_market_overview
from utils.graph_utils import generate_price_graph
from data.data_handler import fetch_crypto_data
from gui.gui_main import CryptoTrackerApp
import tkinter as tk


def fetch_crypto_data():
    """
    Fetch real-time cryptocurrency data from the CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 50}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []


if __name__ == "__main__":
    # Fetch initial data
    crypto_data = fetch_crypto_data()
    if not crypto_data:
        print("Failed to fetch data. Exiting.")
    else:
        # Initialize the Tkinter root window
        root = tk.Tk()
        
        # Initialize and run the CryptoTrackerApp with crypto data
        app = CryptoTrackerApp(root, crypto_data)
        
        # Start the main loop for the app
        root.mainloop()

        # If you want the terminal-based functionality to run in parallel, you'd need a threading mechanism
        # or manage the timing with the tkinter app's event loop. Below shows a terminal-based function that 
        # could be run separately if desired.

        while True:
            # Fetch real-time cryptocurrency data
            data = fetch_crypto_data()

            # Top Gainers and Losers
            top_gainers, top_losers = get_top_gainers_and_losers(data)
            print("\nTop Gainers:")
            for coin in top_gainers:
                print(f"{coin['name']}: {coin['price_change_percentage_24h']}%")

            print("\nTop Losers:")
            for coin in top_losers:
                print(f"{coin['name']}: {coin['price_change_percentage_24h']}%")

            # Currency Conversion
            try:
                amount = float(input("Enter amount to convert: "))
                from_currency = input("Enter cryptocurrency symbol (e.g., 'btc'): ").lower()
                to_currency = input("Enter target currency (default 'usd'): ").lower() or "usd"
                converted_amount = convert_currency(amount, from_currency, to_currency, data)
                if converted_amount:
                    print(f"{amount} {from_currency.upper()} is equal to {converted_amount} {to_currency.upper()}")
            except ValueError:
                print("Invalid amount entered for conversion.")

            # Price Alerts
            try:
                target_price = float(input("Enter the target price: "))
                crypto_id = input("Enter the cryptocurrency id (e.g., 'bitcoin'): ").lower()
                set_price_alert(target_price, crypto_id, data)
            except ValueError:
                print("Invalid target price entered.")

            # Market Overview
            display_market_overview(data)

            # Generate and Display Graph of Price Trends
            print("\nGenerating Price Graph...")
            generate_price_graph(data)

            # Pause for 60 seconds before refreshing data
            time.sleep(60)
