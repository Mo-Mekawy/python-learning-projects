from time import sleep
import requests

# needed params
api_key = "4e6d63a5-a7ea-4f89-861f-ebd8089b0abe"
bot_key = "your bot key"
chat_id = "the bot chat id"
# the time between requests
time_period = 260


def main():
    # get the price of bitcoin on the program opening and check its valid
    old_price = btc_price()
    while old_price == None:
        old_price = btc_price()

    while True:
        price = btc_price()  # get the new price every iterate
        if price != None:
            # if the btc price is getting lower send a message
            if price < old_price:
                send_update(
                    f"Bit coin price has decreased from {old_price} to {price}")
                old_price = price
            # if the btc price is getting heigher send a message
            elif price > old_price:
                send_update(
                    f"Bit coin price has increased from {old_price} to {price}")
                old_price = price
            # take a time beween every request to the web
            sleep(time_period)


def send_update(msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"

    try:
        requests.get(url)
    except (ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
        print(e)


def btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/category'
    parameters = {
        "id": "605e2ce9d41eae1066535f7c",
        'start': '1',
        'limit': '1',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        response = requests.get(url, headers=headers,
                                params=parameters).json()
    except (ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
        print(e)
    else:
        return response["data"]["coins"][0]["quote"]["USD"]["price"]


main()
