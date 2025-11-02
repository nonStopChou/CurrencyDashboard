import os
from dotenv import load_dotenv

load_dotenv()


# === Base directories ===

BASE_DIR = 'data'
DATASET_DIR = 'dataset'
RAW_DATA_DIR = 'raw'
RAW_HISTORY = 'history'
RAW_LATEST = 'latest'
PROCCESS_DIR = "proccessed"

# === API Settings ===
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
EXCHANGE_RATE_BASE_CURRENCY = os.getenv("EXCHANGE_RATE_BASE_CURRENCY", "TWD")
BACKEND_BASE_URL = os.getenv(
    "BACKEND_BASE_URL", 
    f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}"
)


# === Currency ===
INDEX_COLUMN = "timestamp"
BASE_COLUMNS = ['base_currency']
TARGET_CURRENCY = "USD"
TARGET_CURRENCY_LIST = ["USD","EUR","JPY","GBP","CNY","AUD","CAD","CHF","HKD","SGD","SEK","KWR","NOK","NZD","INR","MXN","TWD","ZAR","BRL","DKK","PLN","THB","ILS","IDR","CZK","AED","TRY","HUF","CLP","SAR","PHP","MYR","COP","RUB","RON","PEN","BHD","BGN","ARS"]
