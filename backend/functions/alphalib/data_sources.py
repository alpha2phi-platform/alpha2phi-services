import json
import time

import boto3
import investpy
import pandas as pd

from .config import COUNTRIES_TABLE_NAME, STOCKS_TABLE_NAME
from .logger import LOGGER


def get_stock_info(symbol, country):
    try:
        return investpy.get_stock_information(symbol, country)
    except Exception as e:
        LOGGER.exception(f"Error getting stock for {country} {symbol}", e)
        return pd.DataFrame()


def get_all_stocks_info(stocks):
    stocks_info = None
    count = 0
    for _, row in stocks.iterrows():
        count = count + 1
        stock = get_stock_info(row.symbol, row.country)
        if stock is None:
            continue
        if stocks_info is None:
            stocks_info = stock
        else:
            stocks_info = stocks_info.append(stock)
        if count % 10 == 0:
            print(f"Saving {count}/{len(stocks)}")
            # save_csv(df_stocks_info, STOCKS_INFO_DATASET)
            time.sleep(3)
    # save_csv(df_stocks_info, STOCKS_INFO_DATASET)


def update_countries(countries):
    dynamodb = boto3.resource("dynamodb")
    countries_table = dynamodb.Table(COUNTRIES_TABLE_NAME)
    with countries_table.batch_writer() as batch:
        for country in countries:
            item = {"country": country}
            batch.put_item(Item=item)


def update_stocks(stocks):
    dynamodb = boto3.resource("dynamodb")
    stocks_table = dynamodb.Table(STOCKS_TABLE_NAME)
    with stocks_table.batch_writer() as batch:
        for _, row in stocks.iterrows():
            batch.put_item(json.loads(row.to_json()))


# def update_stock(row):
#     """Update stock table
#
#     Args:
#         row : Stock.
#     """
#     item = {
#         "country": row[0],
#         "symbol": row[5],
#         "name": row[1],
#         "full_name": row[2],
#         "isin": row[3],
#         "currency": row[4],
#     }
#     print(item)
#     stocks_table.put_item(Item=item)
