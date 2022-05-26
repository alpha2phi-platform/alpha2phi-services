from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Stock:
    """
    Stock class
    """

    symbol: str
    name: str
    full_name: str
    currency: str
    country: str
    isin: str
    update_datetime: datetime
    update_datetime_isoformat: str
    info_update_datetime: datetime = datetime.min
    info_update_datetime_isoformat: str = datetime.min.isoformat()


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
