from pycoingecko import CoinGeckoAPI

coin =CoinGeckoAPI()

coing= coin.get_coins_markets(vs_currency='eur')
