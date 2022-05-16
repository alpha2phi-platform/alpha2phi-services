import os
import sys
import unittest
import unittest.mock

import pandas as pd

# Set the library path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from alphalib import LOGGER, get_stock_info


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

    def test_logger(self):
        LOGGER.info("test_logger")

    def test_get_stock(self):
        stocks: pd.DataFrame = get_stock_info("AAPL", "united states")
        print(stocks.head(10))
