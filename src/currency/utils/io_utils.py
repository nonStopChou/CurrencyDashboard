import os
import pandas as pd
import json 

def create_folder_if_not_exist(path):
    print(f"⭕ Check folder exist : {path}")
    if not os.path.exists(path):
        os.mkdir(path)


def append_to_excel(df_old, df_new) -> pd.DataFrame:
    if df_old is None or df_old.empty:
        return df_new
    else:
        duplicate = df_new['timestamp'].isin(df_old['timestamp']).any()
        # print(f"✅ ({0 if duplicate else 1} rows appended)")
        if not duplicate:
            return pd.concat([df_old, df_new], ignore_index = True)
        return df_old
    
def load_excel(filepath) -> pd.DataFrame | None:
    # print(f"✅  Load Excel from {filepath}")
    
    if os.path.exists(filepath):
        print(f"Read xlsx from {filepath}")
        return pd.read_excel(filepath, engine="openpyxl")
    else:
        return None
    
def save_rawdata(path, rawJson):    
    with open(path, 'w') as f:
        json.dump(rawJson, f)
    # print("✅ Save RawData Success.")

