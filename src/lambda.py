import os

import boto3
import investpy


def handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    TABLE_NAME = os.environ["STOCKS_TABLE"]
    table = dynamodb.Table(TABLE_NAME)
    df = investpy.stocks.get_stocks("united states")
    for _, row in df.iterrows():
        item = {
            "country": row[0],
            "name": row[1],
            "full_name": row[2],
            "isin": row[3],
            "currency": row[4],
            "symbol": row[5],
        }
        print(item)
        table.put_item(Item=item)

    return {}
