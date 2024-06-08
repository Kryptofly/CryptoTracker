import requests

def get_crypto_price(crypto):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[crypto]['usd']

def main():
    cryptos = ['bitcoin', 'ethereum', 'dogecoin']
    for crypto in cryptos:
        price = get_crypto_price(crypto)
        print(f'The current price of {crypto.capitalize()} is ${price}')

if __name__ == "__main__":
    main()
