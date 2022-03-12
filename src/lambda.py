import os

import boto3
import investpy

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ["STOCKS_TABLE"]
table = dynamodb.Table(TABLE_NAME)

def update_stock(row):
    item = {
        "country": row[0],
        "symbol": row[5],
        "name": row[1],
        "full_name": row[2],
        "isin": row[3],
        "currency": row[4],
    }
    print(item)
    table.put_item(Item=item)


def handler(event, context):
    df = investpy.stocks.get_stocks("united states")
    df.apply(update_stock, axis=1)
    return {}
