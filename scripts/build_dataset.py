import argparse
from src.currency.utils.io_utils import create_folder_if_not_exist
from src.currency.config.config import (
    BASE_DIR, RAW_DATA_DIR, DATASET_DIR
)

from src.currency.data.builder import build_dataset

def init_folder():
    create_folder_if_not_exist(BASE_DIR)
    create_folder_if_not_exist(f"{BASE_DIR}/{DATASET_DIR}")
    create_folder_if_not_exist(f"{BASE_DIR}/{RAW_DATA_DIR}")

def main():

    parser = argparse.ArgumentParser(description="Get historical currency")
    parser.add_argument("--source", help="source data fodler [history or latest]", default="history")
    parser.add_argument("--output", help="output filename", default="dataset_historical_currency")
    parser.add_argument("--base_currency", help="base currency json source", default="TWD")
    args = parser.parse_args()

    if args.source not in ['history', 'latest']:
        print("Source must be history or latest")
        return 
    
    base_currency = args.base_currency.upper()

    create_folder_if_not_exist(f"{BASE_DIR}/{RAW_DATA_DIR}/{args.source}/{base_currency}")
    create_folder_if_not_exist(f"{BASE_DIR}/{DATASET_DIR}/{base_currency}")
    
    source_path = f"./{BASE_DIR}/{RAW_DATA_DIR}/{args.source}/{base_currency}"
    output_file_path = f"./{BASE_DIR}/{DATASET_DIR}/{base_currency}/{args.output}.xlsx"

    build_dataset(base_currency=base_currency, source=args.source, source_path=source_path, output_path=output_file_path)

if __name__ == "__main__":
    main()