 import matplotlib.pyplot as plt

def plot_price_trend(names, prices):
    plt.bar(names, prices, color='blue')
    plt.xlabel("Cryptocurrency")
    plt.ylabel("Price (USD)")
    plt.title("Cryptocurrency Prices")
    plt.show()

