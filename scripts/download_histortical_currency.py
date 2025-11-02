import time
import argparse
import os
from datetime import timedelta
from tqdm import tqdm
from src.currency.config.config import (
    BASE_DIR, RAW_DATA_DIR, DATASET_DIR, RAW_HISTORY, TARGET_CURRENCY
)

from src.currency.utils.io_utils import save_rawdata, create_folder_if_not_exist
from src.currency.utils.time_utils import get_file_name, string_to_date
from src.currency.api.fetch_currency import fetch_history_currency


def init_folder():
    create_folder_if_not_exist(BASE_DIR)
    create_folder_if_not_exist(f"{BASE_DIR}/{RAW_DATA_DIR}")
    create_folder_if_not_exist(f"{BASE_DIR}/{RAW_DATA_DIR}/{RAW_HISTORY}")
    create_folder_if_not_exist(f"{BASE_DIR}/{DATASET_DIR}")
    

def main():

    parser = argparse.ArgumentParser(description="Get historical currency")
    parser.add_argument("--base_currency", help="Currency details can be found in https://www.exchangerate-api.com/docs/supported-currencies", default=TARGET_CURRENCY)
    parser.add_argument("--start_date", help="with format YYYY/MM/DD")
    parser.add_argument("--end_date", help="with format YYYY/MM/DD")
    args = parser.parse_args()

    init_folder()

    start_date = string_to_date(args.start_date)
    end_date = string_to_date(args.end_date)
    if not start_date or not end_date:
        print("Start Date and End Date must be set.")
        return 
    

    diff_day = (end_date - start_date).days

    current_date = start_date
    
    base_currency = args.base_currency.upper()

    create_folder_if_not_exist(f"{BASE_DIR}/{RAW_DATA_DIR}/{RAW_HISTORY}/{base_currency}")

    try: 
        bar = tqdm(range(diff_day), desc="Proccessing: ")
        for _ in bar:
            bar.set_postfix({"current" : f"Fetch Date {current_date}"})

            rawdata_filename = get_file_name(current_date)

            file_path = f"./{BASE_DIR}/{RAW_DATA_DIR}/{RAW_HISTORY}/{base_currency}/{rawdata_filename}"
            
            if not os.path.exists(file_path):
                jsonData = fetch_history_currency(base_currency=base_currency, input_date=current_date)
                save_rawdata(file_path, jsonData)
                time.sleep(0.15)

            current_date += timedelta(days = 1)
            
    except Exception as error:
        print(f"Exception Occurred. {error}")


if __name__ == "__main__":
    main()