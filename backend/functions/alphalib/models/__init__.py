from dataclasses import dataclass
from datetime import datetime, timezone


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
    update_datetime: float
    update_datetime_isoformat: str
    info_update_datetime: float = datetime.min.replace( tzinfo=timezone.utc).timestamp()  
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
