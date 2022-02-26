import unittest

from ..myinvestor import MyInvestor


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        with self.assertRaises(TypeError):
            s.split(" ")

    def test_get_stock(self):
        symbol = "AAPL"
        myinvestor = MyInvestor()
        myinvestor.get_stock_info(symbol)


if __name__ == "__main__":
    unittest.main()
