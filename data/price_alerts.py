# data/price_alerts.py

def set_price_alert(target_price, crypto_id, data):
    for coin in data:
        if coin['id'] == crypto_id and coin['current_price'] >= target_price:
            print(f"Alert: {coin['name']} has reached the target price of ${target_price}")
            return True
    print(f"{crypto_id} has not reached the target price of ${target_price}")
    return False

