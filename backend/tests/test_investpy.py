import os
import re
import time
import unittest
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import List

import investpy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta

# Global variables and constants
COUNTRY = "united states"
DATASET_FOLDER = "test_data"
TARGET_DATASET_FOLDER = f"{DATASET_FOLDER}/{COUNTRY}"
STOCKS_DATASET = f"{TARGET_DATASET_FOLDER}/stocks.csv"
STOCKS_INFO_DATASET = f"{TARGET_DATASET_FOLDER}/stocks_info.csv"
STOCKS_FINANCE_DATASET = f"{TARGET_DATASET_FOLDER}/stocks_finance.csv"
STOCKS_DIVIDENDS_DATASET = f"{TARGET_DATASET_FOLDER}/stocks_dividends.csv"
STOCKS_SELECTED = f"{TARGET_DATASET_FOLDER}/stocks_selected.csv"


def create_folder(folder):
    """Create folder if not exists"""
    if not os.path.exists(folder):
        os.makedirs(folder)


def save_csv(df, file_name):
    df.to_csv(file_name, header=True, index=False)


def get_stock_info(symbol, country):
    try:
        return investpy.get_stock_information(symbol, country)
    except:
        return None


def get_stock_dividends(symbol, country):
    try:
        return investpy.get_stock_dividends(symbol, country)
    except:
        return None


def read_csv(file):
    if not os.path.isfile(file):
        return None
    return pd.read_csv(file)


def download_stocks_info(df):
    df_stocks_info = None
    count = 0
    for _, row in df.iterrows():
        count = count + 1
        # print(f"{count}/{len(df)}: {row.symbol}-{row['name']}")
        df_stock = get_stock_info(row.symbol, row.country)
        if df_stock is None:
            continue
        if df_stocks_info is None:
            df_stocks_info = df_stock
        else:
            df_stocks_info = df_stocks_info.append(df_stock)
        if count % 10 == 0:
            print(f"Saving {count}/{len(df)}")
            save_csv(df_stocks_info, STOCKS_INFO_DATASET)
            time.sleep(3)
    save_csv(df_stocks_info, STOCKS_INFO_DATASET)


def download_stocks_dividends(df):
    df_stocks_dividends = None
    count = 0
    for _, row in df.iterrows():
        count = count + 1
        # print(f"{count}/{len(df)}: {row.symbol}-{row['name']}")
        df_stock = get_stock_dividends(row.symbol, row.country)
        if df_stock is None:
            continue
        df_stock["Symbol"] = row.symbol
        if df_stocks_dividends is None:
            df_stocks_dividends = df_stock
        else:
            df_stocks_dividends = df_stocks_dividends.append(df_stock)
        if count % 10 == 0:
            print(f"Saving {count}/{len(df)}")
            save_csv(df_stocks_dividends, STOCKS_DIVIDENDS_DATASET)
            time.sleep(3)
    save_csv(df_stocks_dividends, STOCKS_DIVIDENDS_DATASET)


class TestInvestPy(unittest.TestCase):
    """Test out the investpy library

    - EPS
    - P/E
    - PEG
    - FCF
    - P/B
    - ROE
    - DPR
    - P/S
    - DYR
    - DE

    """

    @unittest.skip("Skip setup")
    def setUp(self):
        # Cretarget folder
        create_folder(TARGET_DATASET_FOLDER)

    @unittest.skip("skip get stocks")
    def test_get_stocks(self):
        # Get stocks for the country
        stocks = investpy.get_stocks(country=COUNTRY)

        # Save stock list
        save_csv(stocks, STOCKS_DATASET)
