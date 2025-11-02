import argparse

from src.currency.config.config import (
    BASE_DIR, 
    DATASET_DIR,
    TARGET_CURRENCY,
    TARGET_CURRENCY_LIST,
    BASE_COLUMNS,
    PROCCESS_DIR,
    INDEX_COLUMN
)

from src.currency.data.processor import (
    preproccessing
)

def main():
    
    parser = argparse.ArgumentParser(description="Pre-proccess the dataset.")
    parser.add_argument("--dataset", help="the xlsx dataset's name under dataset folder", default="dataset_historical_currency")
    parser.add_argument("--base_currency", help="the base currency under the dataset folder", default="TWD")
    args = parser.parse_args()

    base_currency = args.base_currency.upper()

    dataset_path = f"./{BASE_DIR}/{DATASET_DIR}/{base_currency}"
    proccessed_path = f"./{BASE_DIR}/{PROCCESS_DIR}/{base_currency}"
    
    file_path = f"{dataset_path}/{args.dataset}.xlsx"
    result_path = f"{proccessed_path}/{args.dataset}-proccess.xlsx"

    col_to_keep = [INDEX_COLUMN] + BASE_COLUMNS + [TARGET_CURRENCY] + TARGET_CURRENCY_LIST
    
    preproccessing(dataset_path=file_path, base_currency=base_currency, output_path=result_path, index_column=INDEX_COLUMN, col_to_keep=col_to_keep)


if __name__ == "__main__":
    main()