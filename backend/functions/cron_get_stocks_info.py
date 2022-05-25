import json
from dataclasses import asdict
from decimal import Decimal

import boto3

from .alphalib import STOCKS_INFO_TABLE_NAME, STOCKS_TABLE_NAME
from .alphalib.data_sources import get_stock_info, sanitized_column_name
from .alphalib.models import Stock
from .alphalib.utils import (convert_iso_format, days_diff,
                             get_current_time_utc, logger, parse_datetime)

DAYS_LAST_UPDATE = 10


def handler(event, context):

    # Get all stocks from databae
    dynamodb = boto3.resource("dynamodb")
    stocks_table = dynamodb.Table(STOCKS_TABLE_NAME)

    response = stocks_table.scan()

    stocks = response["Items"]
    count = response["Count"]

    # Convert from list of objects to data frame - TODO:

    # Get info for each stock
    logger.info(f"Total stocks - {count}")
    now = get_current_time_utc()

    # Dividend table
    dynamodb = boto3.resource("dynamodb")
    stocks_info_table = dynamodb.Table(STOCKS_INFO_TABLE_NAME)

    new_column_names = []
    for row in stocks:
        stock = Stock(**row)
        days_since_last_update = days_diff(
            parse_datetime(stock.info_update_datetime), now
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
            stock.info_update_datetime = convert_iso_format(get_current_time_utc())
            stocks_table.put_item(Item=asdict(stock))

        break

    # Get stocks dividends - TODO:

    return {}
