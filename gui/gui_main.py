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

        
        self.root.configure(bg="#2a2a2a")

        
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "TNotebook",
            background="#2a2a2a",
            foreground="white",
            padding=10,
        )
        style.configure(
            "TNotebook.Tab",
            background="#1e1e1e",
            foreground="white",
            font=("Arial", 12, "bold"),
            padding=[10, 5],
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", "#0078D4")],
            foreground=[("selected", "white")],
        )
        style.configure(
            "TFrame",
            background="#2a2a2a",
        )

        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, pady=10)

        
        self.tab_overview = ttk.Frame(self.notebook, style="TFrame")
        self.tab_gainers_losers = ttk.Frame(self.notebook, style="TFrame")
        self.tab_converter = ttk.Frame(self.notebook, style="TFrame")
        self.tab_alerts = ttk.Frame(self.notebook, style="TFrame")
        self.tab_graphs = ttk.Frame(self.notebook, style="TFrame")

        
        self.notebook.add(self.tab_overview, text="Market Overview")
        self.notebook.add(self.tab_gainers_losers, text="Gainers & Losers")
        self.notebook.add(self.tab_converter, text="Currency Converter")
        self.notebook.add(self.tab_alerts, text="Price Alerts")
        self.notebook.add(self.tab_graphs, text="Graphs")

       
        self.setup_overview_tab()
        self.setup_gainers_losers_tab()
        self.setup_converter_tab()
        self.setup_alerts_tab()
        self.setup_graphs_tab()

    def create_styled_button(self, parent, text, command):
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg="#0078D4",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="raised",
            activebackground="#005A9E",
            activeforeground="white",
            bd=2,
            padx=10,
            pady=5,
        )

    def create_styled_label(self, parent, text, font_size=16):
        return tk.Label(
            parent,
            text=text,
            font=("Arial", font_size),
            bg="#2a2a2a",
            fg="white",
            wraplength=500,  
            justify="center",  
        )

    def setup_overview_tab(self):
        self.create_styled_label(self.tab_overview, "Market Overview").pack(pady=10)

        overview_text = tk.Text(
            self.tab_overview,
            wrap="word",
            height=15,
            width=60,
            bg="#1e1e1e",
            fg="white",
            font=("Arial", 12),
        )
        overview_text.pack(pady=10)

        def refresh_overview():
            overview = display_market_overview(self.crypto_data)
            overview_text.delete("1.0", tk.END)
            overview_text.insert(tk.END, overview)

        refresh_button = self.create_styled_button(self.tab_overview, "Refresh Overview", refresh_overview)
        refresh_button.pack(pady=10)

    def setup_gainers_losers_tab(self):
        self.create_styled_label(self.tab_gainers_losers, "Top Gainers & Losers").pack(pady=10)

        gainers_text = tk.Text(
            self.tab_gainers_losers,
            wrap="word",
            height=10,
            width=60,
            bg="#1e1e1e",
            fg="white",
            font=("Arial", 12),
        )
        gainers_text.pack(pady=10)
        losers_text = tk.Text(
            self.tab_gainers_losers,
            wrap="word",
            height=10,
            width=60,
            bg="#1e1e1e",
            fg="white",
            font=("Arial", 12),
        )
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

        refresh_button = self.create_styled_button(self.tab_gainers_losers, "Refresh Data", refresh_gainers_losers)
        refresh_button.pack(pady=10)

    def setup_converter_tab(self):
        self.create_styled_label(self.tab_converter, "Currency Converter").pack(pady=10)

        self.create_styled_label(self.tab_converter, "Enter amount:", font_size=12).pack(pady=5)
        amount_entry = tk.Entry(self.tab_converter, font=("Arial", 12), bg="#1e1e1e", fg="white")
        amount_entry.pack(pady=5)

        self.create_styled_label(self.tab_converter, "Enter cryptocurrency symbol (e.g., 'btc'):", font_size=12).pack(
            pady=5
        )
        from_currency_entry = tk.Entry(self.tab_converter, font=("Arial", 12), bg="#1e1e1e", fg="white")
        from_currency_entry.pack(pady=5)

        self.create_styled_label(self.tab_converter, "Enter target currency (default 'usd'):", font_size=12).pack(pady=5)
        to_currency_entry = tk.Entry(self.tab_converter, font=("Arial", 12), bg="#1e1e1e", fg="white")
        to_currency_entry.pack(pady=5)

        result_label = self.create_styled_label(self.tab_converter, "", font_size=12)
        result_label.pack(pady=10)

        def convert():
            try:
                amount = float(amount_entry.get())
                from_currency = from_currency_entry.get().lower()
                to_currency = to_currency_entry.get().lower() or "usd"
                converted_amount = convert_currency(amount, from_currency, to_currency, self.crypto_data)
                if converted_amount:
                    result_label.config(
                        text=f"{amount} {from_currency.upper()} = {converted_amount} {to_currency.upper()}"
                    )
                else:
                    result_label.config(text="Conversion failed! Check input values.")
            except ValueError:
                result_label.config(text="Please enter a valid amount.")

        convert_button = self.create_styled_button(self.tab_converter, "Convert", convert)
        convert_button.pack(pady=10)

    def setup_alerts_tab(self):
        self.create_styled_label(self.tab_alerts, "Price Alerts").pack(pady=10)

        self.create_styled_label(self.tab_alerts, "Enter target price:", font_size=12).pack(pady=5)
        target_price_entry = tk.Entry(self.tab_alerts, font=("Arial", 12), bg="#1e1e1e", fg="white")
        target_price_entry.pack(pady=5)

        self.create_styled_label(self.tab_alerts, "Enter cryptocurrency ID (e.g., 'bitcoin'):", font_size=12).pack(pady=5)
        crypto_id_entry = tk.Entry(self.tab_alerts, font=("Arial", 12), bg="#1e1e1e", fg="white")
        crypto_id_entry.pack(pady=5)

        alert_label = self.create_styled_label(self.tab_alerts, "", font_size=12)
        alert_label.pack(pady=10)

        def set_alert():
            try:
                target_price = float(target_price_entry.get())
                crypto_id = crypto_id_entry.get().lower()
                alert_set = set_price_alert(target_price, crypto_id, self.crypto_data)
                if alert_set:
                    alert_label.config(
                        text=f"Alert set for {crypto_id.capitalize()} at ${target_price}."
                    )
                else:
                    alert_label.config(text="Failed to set alert! Check input values.")
            except ValueError:
                alert_label.config(text="Please enter a valid price.")

        alert_button = self.create_styled_button(self.tab_alerts, "Set Alert", set_alert)
        alert_button.pack(pady=10)

    def setup_graphs_tab(self):
        self.create_styled_label(self.tab_graphs, "Cryptocurrency Price Graphs").pack(pady=10)

        self.create_styled_label(self.tab_graphs, "Enter cryptocurrency ID (e.g., 'bitcoin'):", font_size=12).pack(
            pady=5
        )
        graph_crypto_id_entry = tk.Entry(self.tab_graphs, font=("Arial", 12), bg="#1e1e1e", fg="white")
        graph_crypto_id_entry.pack(pady=5)

        graph_label = self.create_styled_label(self.tab_graphs, "", font_size=12)
        graph_label.pack(pady=10)

        def plot_graph():
            crypto_id = graph_crypto_id_entry.get().lower()
            success = generate_price_graph(crypto_id, self.crypto_data)
            if success:
                graph_label.config(text="Graph generated successfully!")
            else:
                graph_label.config(text="Failed to generate graph! Check input values.")

        graph_button = self.create_styled_button(self.tab_graphs, "Generate Graph", plot_graph)
        graph_button.pack(pady=10)


if __name__ == "__main__":
    
    crypto_data = {"bitcoin": {"price": 45000}, "ethereum": {"price": 3000}}
    root = tk.Tk()
    app = CryptoTrackerApp(root, crypto_data)
    root.mainloop()
