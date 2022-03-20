import json
import unittest

import investpy


class TestInvestpy(unittest.TestCase):
    """Test investpy library"""

    def test_get_stock_countries(self):
        """Get stock countries"""
        countries = investpy.stocks.get_stock_countries()
        print(countries)
        self.assertGreater(len(countries), 0)

    def test_get_stocks_for_country(self):
        """Get stocks for a country"""
        df = investpy.stocks.get_stocks("united states")
        for _, row in df.iterrows():
            print(json.loads(row.to_json()))
        self.assertGreater(len(df), 0)


if __name__ == "__main__":
    unittest.main()
