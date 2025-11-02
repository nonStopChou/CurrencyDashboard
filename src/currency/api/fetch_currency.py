import argparse
from src.currency.config.config import (
    BASE_DIR, RAW_DATA_DIR, BACKEND_BASE_URL, RAW_LATEST
)
from src.currency.utils.io_utils import (
    save_rawdata,
    create_folder_if_not_exist,
)

from src.currency.api.client import get_request

def fetch_today_currency(base_currency: str):

    base_currency = base_currency.upper()

    create_folder_if_not_exist(f"./{BASE_DIR}/{RAW_DATA_DIR}/{RAW_LATEST}/{base_currency}")

    url = f"{BACKEND_BASE_URL.rstrip("/")}/latest/{base_currency}"

    return get_request(url)

def fetch_history_currency(base_currency: str, input_date: str):

    url = f"{BACKEND_BASE_URL.rstrip("/")}/history/{base_currency}/{input_date.year}/{input_date.month}/{input_date.day}"

    jsonData = get_request(url)

    return jsonData
