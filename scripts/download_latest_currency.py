import argparse
from src.currency.config.config import (
    BASE_DIR, RAW_DATA_DIR, DATASET_DIR,
    RAW_LATEST, TARGET_CURRENCY
)
from src.currency.utils.io_utils import save_rawdata, create_folder_if_not_exist
from src.currency.utils.time_utils import get_file_name
from src.currency.api.fetch_currency import fetch_today_currency

def init_folder():
    create_folder_if_not_exist(BASE_DIR)
    create_folder_if_not_exist(f"{BASE_DIR}/{RAW_DATA_DIR}")
    create_folder_if_not_exist(f"{BASE_DIR}/{RAW_DATA_DIR}/{RAW_LATEST}")
    create_folder_if_not_exist(f"{BASE_DIR}/{DATASET_DIR}")

def main():

    parser = argparse.ArgumentParser(description="GET request helper for currency URL endpoints.")
    parser.add_argument("--base_currency", choices=["USD", "AUS", "CNY", "TWD"], help="Currency details can be found in https://www.exchangerate-api.com/docs/supported-currencies", default=TARGET_CURRENCY)
    args = parser.parse_args()

    init_folder()

    jsonData = fetch_today_currency(base_currency=args.base_currency)

    if not jsonData:
        print("No Currency Data was found. please check the application log to check error.")
    else:
        last_update_timestamp = jsonData['time_last_update_unix']
        rawdata_filename = get_file_name(last_update_timestamp)
        file_path = f"./{BASE_DIR}/{RAW_DATA_DIR}/{RAW_LATEST}/{args.base_currency}/{rawdata_filename}"

        save_rawdata(file_path, jsonData)

if __name__ == "__main__":
    main()