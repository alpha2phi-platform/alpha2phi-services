from dataclasses import dataclass
from datetime import datetime, timezone

from ..utils import dateutils


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
    info_update_datetime: float = dateutils.to_epoch_time(datetime.min)
    info_update_datetime_isoformat: str = dateutils.to_isoformat(datetime.min)


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
