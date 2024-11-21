

def get_top_gainers_and_losers(data):
    
    gainers = [coin for coin in data if coin['price_change_percentage_24h'] > 0]
    losers = [coin for coin in data if coin['price_change_percentage_24h'] < 0]

   
    sorted_gainers = sorted(gainers, key=lambda x: x['price_change_percentage_24h'], reverse=True)[:5]
    sorted_losers = sorted(losers, key=lambda x: x['price_change_percentage_24h'])[:5]

    return sorted_gainers, sorted_losers
