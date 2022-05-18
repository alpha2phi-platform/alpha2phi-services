import json
import os
import sys
import unittest
import unittest.mock

# Set the library path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from alphalib import (get_stock_countries, get_stock_dividends, get_stock_info,
                      logger, sanitized_column_name)


class TestAlphalib(unittest.TestCase):
    """Test out the alphalib library

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

    def setUp(self):
        print("\n---------------- Test Start ----------------\n")

    def tearDown(self):
        print("\n---------------- Test End ----------------\n")

    @unittest.skip("Skipped")
    def test_logger(self):
        logger.info("test_logger")

    @unittest.skip("Skipped")
    def test_get_stock_countries(self):
        logger.info(get_stock_countries())

    @unittest.skip("Skipped")
    def test_get_stock_info(self):
        stocks = get_stock_info("AAPL", "united states")
        column_names = stocks.columns.to_list()
        new_column_names = []
        for name in column_names:
            new_column_names.append(sanitized_column_name(name))
        stocks.columns = new_column_names
        print(stocks.head(1))

        # for _, row in stocks.iterrows():
        #     logger.info(json.loads(row.to_json()))

    # @unittest.skip("Skipped")
    def test_get_stock_dividends(self):
        stocks_dividends = get_stock_dividends("GM", "united states")
        print(stocks_dividends.columns.to_list())
        column_names = stocks_dividends.columns.to_list()
        new_column_names = []
        for name in column_names:
            new_column_names.append(sanitized_column_name(name))
        stocks_dividends.columns = new_column_names
        print(stocks_dividends.head(1))

    @unittest.skip("Skipped")
    def test_sanitize_column_name(self):
        print(sanitized_column_name("123 (a..) P/E-"))
