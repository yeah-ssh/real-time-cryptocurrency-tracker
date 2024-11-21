
def convert_currency(amount, from_currency, to_currency, data):
    conversion_rate = None
    for coin in data:
        if coin['symbol'] == from_currency:
            conversion_rate = coin['current_price']
            break

    if conversion_rate:
        converted_amount = amount * conversion_rate
        return round(converted_amount, 2)
    else:
        print(f"Error: {from_currency.upper()} not found in the data.")
        return None
 
