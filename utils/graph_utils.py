import matplotlib.pyplot as plt

def generate_price_graph(crypto_id=None, crypto_data=None):
    if crypto_data is None or len(crypto_data) == 0:
        print("Error: No cryptocurrency data provided.")
        return False

    if crypto_id:
        # Filter data for the specified crypto_id
        filtered_data = [coin for coin in crypto_data if coin['id'].lower() == crypto_id.lower()]
        if not filtered_data:
            print(f"Error: Cryptocurrency with ID '{crypto_id}' not found.")
            return False

        coin_names = [filtered_data[0]['name']]
        coin_prices = [filtered_data[0]['current_price']]
        title = f"Price Trend for {filtered_data[0]['name']}"
    else:
        
        coin_names = [coin['name'] for coin in crypto_data]
        coin_prices = [coin['current_price'] for coin in crypto_data]
        title = "Cryptocurrency Price Trends"

   
    plt.figure(figsize=(10, 5))
    plt.plot(coin_names, coin_prices, marker='o', linestyle='-', color='blue', label='Price (USD)')
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel("Cryptocurrency", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, fontsize=10)
    plt.legend(loc='upper left')
    plt.tight_layout()

    plt.show()
    return True
