import json
from dataclasses import asdict
from decimal import Decimal

import boto3
import pandas as pd

from .alphalib import STOCKS_INFO_TABLE_NAME, STOCKS_TABLE_NAME
from .alphalib.data_sources import get_stock_info, sanitized_column_name
from .alphalib.models import Stock
from .alphalib.utils import dateutils
from .alphalib.utils.logger import logger

DAYS_LAST_UPDATE = 10


def get_stocks_from_db() -> pd.DataFrame:
    """Get all stocks from database

    Returns:
        Pandas DataFrame
    """

    # Stocks table
    dynamodb = boto3.resource("dynamodb")
    stocks_table = dynamodb.Table(STOCKS_TABLE_NAME)

    # Current time
    current_time = dateutils.current_time_utc()

    # response = stocks_table.scan()
    # stocks = response["Items"]
    # count = response["Count"]

    # Convert from list of objects to data frame - TODO:

    return pd.DataFrame()


def handler(event, context):

    # Get all stocks from databae
    # dynamodb = boto3.resource("dynamodb")
    # stocks_table = dynamodb.Table(STOCKS_TABLE_NAME)
    # response = stocks_table.scan()
    # stocks = response["Items"]
    # count = response["Count"]
    # logger.info(f"Total stocks - {count}")

    # Get a list of stocks to process
    stocks = get_stocks_from_db()
    logger.info(f"Total stocks - {len(stocks)}")

    return {}

    # ----

    # Get info for each stock
    now = dateutils.current_time_utc()

    # Dividend table
    dynamodb = boto3.resource("dynamodb")
    stocks_info_table = dynamodb.Table(STOCKS_INFO_TABLE_NAME)

    new_column_names = []
    count = 0
    for row in stocks:
        stock = Stock(**row)
        days_since_last_update = dateutils.days_diff(
            dateutils.from_epoch_time(stock.info_update_datetime), now
        )
        if days_since_last_update > 10:
            logger.info(f"Getting info for {stock.country} - {stock.symbol}")
            stock_info = get_stock_info(stock.country, stock.symbol)

            # Set the new column name names
            if len(new_column_names) == 0:
                column_names = stock_info.columns.to_list()
                for name in column_names:
                    new_column_names.append(sanitized_column_name(name))

            # Update the stock info
            stock_info.columns = new_column_names
            with stocks_info_table.batch_writer() as batch:
                for _, info in stock_info.iterrows():
                    batch.put_item(json.loads(info.to_json(), parse_float=Decimal))

            # Update the stock update datetime
            stock.info_update_datetime_isoformat = dateutils.to_isoformat(now)
            stock.info_update_datetime = dateutils.to_epoch_time(now)
            stocks_table.put_item(Item=json.loads(stock.to_json(), parse_float=Decimal))

        count = count + 1
        if count == 10:
            break

    # Get stocks dividends - TODO:

    return {}
