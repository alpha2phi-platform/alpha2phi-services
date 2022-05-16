import os

COUNTRY: str = "united states"

# Table names from env variables
STOCKS_TABLE_NAME = os.getenv("STOCKS_TABLE")
COUNTRIES_TABLE_NAME = os.getenv("COUNTRIES_TABLE")
