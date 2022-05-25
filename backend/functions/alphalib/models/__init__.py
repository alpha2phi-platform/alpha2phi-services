from dataclasses import dataclass

# from datetime import datetime
# from typing import Optional


@dataclass
class Stock:
    """
    Stock class
    """

    symbol: str
    name: str
    full_name: str
    info_update_datetime: str
    currency: str
    country: str
    isin: str
    inserted_datetime: str


# TODO: Add more fields
@dataclass
class StockInfo:
    """
    Stock info class
    """


# TODO: Add more fields
@dataclass
class StockDividend:
    """
    Stock dividend class
    """
