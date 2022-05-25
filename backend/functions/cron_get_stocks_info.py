import boto3

from .alphalib import STOCKS_INFO_TABLE_NAME, STOCKS_TABLE_NAME
from .alphalib.data_sources import get_stock_info, sanitized_column_name
from .alphalib.models import Stock
from .alphalib.utils import days_diff, get_current_time_utc, logger


def handler(event, context):

    # Get all stocks from databae
    dynamodb = boto3.resource("dynamodb")
    stocks_table = dynamodb.Table(STOCKS_TABLE_NAME)
    response = stocks_table.scan()
    stocks = response["Items"]
    count = response["Count"]

    # Get info for each stock
    logger.info(f"Total stocks - {count}")
    now = get_current_time_utc()

    # Dividend table
    dynamodb = boto3.resource("dynamodb")
    # stocks_table = dynamodb.Table(STOCKS_INFO_TABLE_NAME)

    new_column_names = []
    for row in stocks:
        stock = Stock(**row)
        days_since_last_update = days_diff(stock.info_update_datetime, now)
        if days_since_last_update > 10:
            logger.info(f"Getting info for {stock.country} - {stock.symbol}")
            stock_info = get_stock_info(stock.country, stock.symbol)

            column_names = stock_info.columns.to_list()
            for name in column_names:
                new_column_names.append(sanitized_column_name(name))
            stock_info.columns = new_column_names
            logger.info(stock_info.columns)
        break

    # Get stocks dividends - TODO:

    return {}
