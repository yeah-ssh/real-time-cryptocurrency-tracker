import tkinter as tk
from tkinter import ttk
from data.gainers_losers import get_top_gainers_and_losers
from data.currency_converter import convert_currency
from data.price_alerts import set_price_alert
from data.market_overview import display_market_overview
from utils.graph_utils import generate_price_graph

class CryptoTrackerApp:
    def __init__(self, root, crypto_data):
        self.root = root
        self.crypto_data = crypto_data
        self.root.title("Real-Time Cryptocurrency Tracker")

        # Notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tabs
        self.tab_overview = ttk.Frame(self.notebook)
        self.tab_gainers_losers = ttk.Frame(self.notebook)
        self.tab_converter = ttk.Frame(self.notebook)
        self.tab_alerts = ttk.Frame(self.notebook)
        self.tab_graphs = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_overview, text="Market Overview")
        self.notebook.add(self.tab_gainers_losers, text="Gainers & Losers")
        self.notebook.add(self.tab_converter, text="Currency Converter")
        self.notebook.add(self.tab_alerts, text="Price Alerts")
        self.notebook.add(self.tab_graphs, text="Graphs")

        # Initialize tab functions
        self.setup_overview_tab()
        self.setup_gainers_losers_tab()
        self.setup_converter_tab()
        self.setup_alerts_tab()
        self.setup_graphs_tab()

    def setup_overview_tab(self):
        tk.Label(self.tab_overview, text="Market Overview", font=("Arial", 16)).pack(pady=10)

        overview_text = tk.Text(self.tab_overview, wrap="word", height=15, width=50)
        overview_text.pack(pady=10)

        def refresh_overview():
            overview = display_market_overview(self.crypto_data)
            overview_text.delete("1.0", tk.END)
            overview_text.insert(tk.END, overview)

        refresh_button = tk.Button(self.tab_overview, text="Refresh Overview", command=refresh_overview)
        refresh_button.pack(pady=10)

    def setup_gainers_losers_tab(self):
        tk.Label(self.tab_gainers_losers, text="Top Gainers & Losers", font=("Arial", 16)).pack(pady=10)

        gainers_text = tk.Text(self.tab_gainers_losers, wrap="word", height=10, width=50)
        gainers_text.pack(pady=10)
        losers_text = tk.Text(self.tab_gainers_losers, wrap="word", height=10, width=50)
        losers_text.pack(pady=10)

        def refresh_gainers_losers():
            gainers, losers = get_top_gainers_and_losers(self.crypto_data)
            gainers_text.delete("1.0", tk.END)
            losers_text.delete("1.0", tk.END)

            gainers_text.insert(tk.END, "Top Gainers:\n")
            for coin in gainers:
                gainers_text.insert(tk.END, f"{coin['name']}: {coin['price_change_percentage_24h']}%\n")

            losers_text.insert(tk.END, "Top Losers:\n")
            for coin in losers:
                losers_text.insert(tk.END, f"{coin['name']}: {coin['price_change_percentage_24h']}%\n")

        refresh_button = tk.Button(self.tab_gainers_losers, text="Refresh Data", command=refresh_gainers_losers)
        refresh_button.pack(pady=10)

    def setup_converter_tab(self):
        tk.Label(self.tab_converter, text="Currency Converter", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_converter, text="Enter amount:").pack()
        amount_entry = tk.Entry(self.tab_converter)
        amount_entry.pack(pady=5)

        tk.Label(self.tab_converter, text="Enter cryptocurrency symbol (e.g., 'btc'):").pack()
        from_currency_entry = tk.Entry(self.tab_converter)
        from_currency_entry.pack(pady=5)

        tk.Label(self.tab_converter, text="Enter target currency (default 'usd'):").pack()
        to_currency_entry = tk.Entry(self.tab_converter)
        to_currency_entry.pack(pady=5)

        result_label = tk.Label(self.tab_converter, text="", font=("Arial", 12))
        result_label.pack(pady=10)

        def convert():
            try:
                amount = float(amount_entry.get())
                from_currency = from_currency_entry.get().lower()
                to_currency = to_currency_entry.get().lower() or "usd"
                converted_amount = convert_currency(amount, from_currency, to_currency, self.crypto_data)
                if converted_amount:
                    result_label.config(text=f"{amount} {from_currency.upper()} = {converted_amount} {to_currency.upper()}")
                else:
                    result_label.config(text="Conversion failed! Check input values.")
            except ValueError:
                result_label.config(text="Please enter a valid amount.")

        convert_button = tk.Button(self.tab_converter, text="Convert", command=convert)
        convert_button.pack(pady=10)

    def setup_alerts_tab(self):
        tk.Label(self.tab_alerts, text="Price Alerts", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.tab_alerts, text="Enter target price:").pack()
        target_price_entry = tk.Entry(self.tab_alerts)
        target_price_entry.pack(pady=5)

        tk.Label(self.tab_alerts, text="Enter cryptocurrency ID (e.g., 'bitcoin'):").pack()
        crypto_id_entry = tk.Entry(self.tab_alerts)
        crypto_id_entry.pack(pady=5)

        alert_label = tk.Label(self.tab_alerts, text="", font=("Arial", 12))
        alert_label.pack(pady=10)

        def set_alert():
            try:
                target_price = float(target_price_entry.get())
                crypto_id = crypto_id_entry.get().lower()
                alert_set = set_price_alert(target_price, crypto_id, self.crypto_data)
                if alert_set:
                    alert_label.config(text=f"Alert set for {crypto_id.upper()} at ${target_price}!")
                else:
                    alert_label.config(text=f"{crypto_id} has not reached the target price yet.")
            except ValueError:
                alert_label.config(text="Please enter a valid target price.")

        alert_button = tk.Button(self.tab_alerts, text="Set Alert", command=set_alert)
        alert_button.pack(pady=10)

    def setup_graphs_tab(self):
        tk.Label(self.tab_graphs, text="Graphs", font=("Arial", 16)).pack(pady=10)

        def show_graph():
            generate_price_graph(self.crypto_data)

        graph_button = tk.Button(self.tab_graphs, text="Show Graph", command=show_graph)
        graph_button.pack(pady=10)
