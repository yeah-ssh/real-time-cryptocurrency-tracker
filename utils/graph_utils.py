import matplotlib.pyplot as plt

def generate_price_graph(crypto_data):
    
    coin_names = [coin['name'] for coin in crypto_data]
    coin_prices = [coin['current_price'] for coin in crypto_data]

    plt.figure(figsize=(10, 5))
    plt.plot(coin_names, coin_prices, marker='o')
    plt.title("Cryptocurrency Price Trends")
    plt.xlabel("Cryptocurrency")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  
