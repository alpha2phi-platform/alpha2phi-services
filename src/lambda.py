import os

import boto3
import investpy

# Table names from env variables
STOCKS_TABLE_NAME = os.environ["STOCKS_TABLE"]
COUNTRIES_TABLE_NAME = os.environ["COUNTIRES_TABLE"]

# Dynamodb tables
dynamodb = boto3.resource("dynamodb")
stocks_table = dynamodb.Table(STOCKS_TABLE_NAME)
countries_table = dynamodb.Table(COUNTRIES_TABLE_NAME)


def update_countries(countries):
    pass


def update_stock(row):
    """Update stock table

    Args:
        row : Stock.
    """
    item = {
        "country": row[0],
        "symbol": row[5],
        "name": row[1],
        "full_name": row[2],
        "isin": row[3],
        "currency": row[4],
    }
    print(item)
    stocks_table.put_item(Item=item)


def handler(event, context):

    countries = investpy.stocks.get_stock_countries()
    print(countries)
    update_countries(countries)

    stocks = investpy.stocks.get_stocks("united states")
    stocks.apply(update_stock, axis=1)

    return {}
