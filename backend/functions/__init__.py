import logging

import boto3
import investpy

COUNTRY: str = "united states"

__name__ = "alphalib"


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


# Create the logger
logger = create_logger()


def get_stock_info(symbol, country):
    try:
        return investpy.get_stock_information(symbol, country)
    except Exception as e:
        logger.exception(f"Error getting stock for {country} {symbol}", e)
        return None


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


# stocks = get_stock_info("AAPL", COUNTRY)
