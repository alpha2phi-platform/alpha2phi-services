import unittest

import investpy


class TestInvestpy(unittest.TestCase):
    """Test investpy library"""

    def test_get_stock_countries(self):
        """Get stock countries"""
        stock_countries = investpy.stocks.get_stock_countries()
        self.assertGreater(len(stock_countries), 0)

    def test_get_stocks_for_country(self):
        """Get stocks for a country"""
        df = investpy.stocks.get_stocks("united states")
        print(df)
        self.assertGreater(len(df), 0)


if __name__ == "__main__":
    unittest.main()
