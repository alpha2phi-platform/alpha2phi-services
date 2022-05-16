import investpy
from alphalib import update_countries, update_stocks


def handler(event, context):

    countries = investpy.stocks.get_stock_countries()
    # print(countries)
    update_countries(countries)

    stocks = investpy.stocks.get_stocks("united states")
    update_stocks(stocks)
    # stocks.apply(update_stock, axis=1)

    return {}
