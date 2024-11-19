from data.data_handler import fetch_crypto_data
from utils.graph_utils import plot_price_trend

def main():
    data = fetch_crypto_data()
    print("Top Cryptocurrencies:")
    for coin in data[:5]:
        print(f"{coin['name']}: ${coin['current_price']}")
    
    # Plot a sample graph
    prices = [coin['current_price'] for coin in data[:7]]
    names = [coin['name'] for coin in data[:7]]
    plot_price_trend(names, prices)

if __name__ == "__main__":
    main()
