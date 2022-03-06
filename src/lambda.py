import os

import boto3
import investpy


def handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    TABLE_NAME = os.environ["STOCKS_TABLE"]
    print("Table name ", TABLE_NAME)
    table = dynamodb.Table(TABLE_NAME)
    df = investpy.stocks.get_stocks("united states")
    print(df)

    return {
        "statusCode": 200,
    }
