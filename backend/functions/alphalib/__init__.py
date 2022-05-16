import os

from .data_sources import update_countries, update_stocks
from .logger import LOGGER

__name__ = "alphalib"

COUNTRY: str = "united states"

# Table names from env variables
STOCKS_TABLE_NAME = os.environ["STOCKS_TABLE"]
COUNTRIES_TABLE_NAME = os.environ["COUNTRIES_TABLE"]
