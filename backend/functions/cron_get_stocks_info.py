import boto3

from .alphalib import STOCKS_TABLE_NAME
from .alphalib.logger import logger
from .alphalib.models import Stock


def handler(event, context):

    # Get all stocks from databae
    dynamodb = boto3.resource("dynamodb")
    stocks_table = dynamodb.Table(STOCKS_TABLE_NAME)
    response = stocks_table.scan()
    stocks = response["Items"]
    count = response["Count"]

    # Get info for each stock
    logger.info(f"Total stocks - {count}")
    for row in stocks:
        stock = Stock(**row)
        print(stock.name)

    # Get stocks dividends - TODO:

    return {}
