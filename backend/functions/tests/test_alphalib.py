import os
import sys
import time
import unittest
import unittest.mock

# Set the library path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from alphalib import (get_current_time_utc, get_stock_countries,
                      get_stock_dividends, get_stock_info, get_stocks, logger,
                      parse_datetime, sanitized_column_name)


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

    def test_set_ts_iso8601(self):
        start = get_current_time_utc()
        time.sleep(1)
        end = get_current_time_utc()

        logger.info(start, end)
        dt = parse_datetime(start)
        print(dt)

    @unittest.skip("Skipped")
    def test_get_stock_countries(self):
        logger.info(get_stock_countries())

    @unittest.skip("Skipped")
    def test_get_stocks(self):
        stocks = get_stocks("united states")
        logger.info(stocks.head(10))

    @unittest.skip("Skipped")
    def test_get_stock_info(self):
        stocks = get_stock_info("AAPL", "united states")
        column_names = stocks.columns.to_list()
        new_column_names = []
        for name in column_names:
            new_column_names.append(sanitized_column_name(name))
        stocks.columns = new_column_names
        logger.info(stocks.head(10))

        # for _, row in stocks.iterrows():
        #     logger.info(json.loads(row.to_json()))

    @unittest.skip("Skipped")
    def test_get_stock_dividends(self):
        stocks_dividends = get_stock_dividends("GM", "united states")
        logger.info(stocks_dividends.columns.to_list())
        column_names = stocks_dividends.columns.to_list()
        new_column_names = []
        for name in column_names:
            new_column_names.append(sanitized_column_name(name))
        stocks_dividends.columns = new_column_names
        logger.info(stocks_dividends.head(1))

    @unittest.skip("Skipped")
    def test_sanitize_column_name(self):
        logger.info(sanitized_column_name("123 (a..) P/E-"))
