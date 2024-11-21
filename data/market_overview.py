def display_market_overview(data):
   
    try:
        total_market_cap = sum(coin['market_cap'] for coin in data if 'market_cap' in coin)
        total_volume = sum(coin['total_volume'] for coin in data if 'total_volume' in coin)
        avg_price_change = sum(coin['price_change_percentage_24h'] for coin in data if 'price_change_percentage_24h' in coin) / len(data)

        overview = (
            f"Total Market Capitalization: ${total_market_cap:,.2f}\n"
            f"Total Volume (24h): ${total_volume:,.2f}\n"
            f"Average Price Change (24h): {avg_price_change:.2f}%\n"
        )
        return overview
    except Exception as e:
        return f"Error generating market overview: {str(e)}"
