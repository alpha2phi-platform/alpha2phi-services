import os
import sys
import unittest
import unittest.mock

import pandas as pd

# Set the library path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from alphalib import get_stock_countries, get_stock_info, logger


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
    def test_get_stock(self):
        print("000")
        stocks: pd.DataFrame = get_stock_info("AAPL", "united states")
        logger.info(stocks.head(10))
