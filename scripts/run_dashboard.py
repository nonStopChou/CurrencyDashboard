import pandas as pd
import argparse
import numpy as np
from src.currency.visualization.components.px_line import line_chart
from src.currency.visualization.components.bar import bar
from src.currency.visualization.components.px_heatmap import heatmap
from src.currency.visualization.dashboard import dashboard

from src.currency.config.config import (
    BASE_DIR,
    DATASET_DIR,
    TARGET_CURRENCY
)

from src.currency.utils.io_utils import (
    load_excel
)

def trend_chart(df: pd.DataFrame, **kwargs):
    return line_chart(df, melt = True, **kwargs)

def normalized_index_chart(df: pd.DataFrame, **kwargs):
    apply = lambda df : df / df.iloc[0] * 100
    return line_chart(df, melt=True, method_apply = apply, **kwargs)
    

def daily_return_chart(df: pd.DataFrame, **kwargs):
    apply = lambda df : df.pct_change() * 100
    return line_chart(df, melt=True, method_apply = apply, **kwargs)


def volatility_barchart(df: pd.DataFrame, **kwargs):
    apply = lambda df : np.round(df.pct_change().std().sort_values(ascending=False) * 100, 4)
    return bar(df, method_apply = apply, **kwargs)


def correlation_heatmap(df: pd.DataFrame, **kwargs):
    apply = lambda df : df.pct_change().dropna().corr()
    return heatmap(df, method_apply = apply, **kwargs)
    

def main():
    
    parser = argparse.ArgumentParser(description="Dashboard of currency dataset")
    parser.add_argument("--debug", default=False)
    parser.add_argument("--dataset", default="dataset_historical_currency-proccess")
    parser.add_argument("--base_currency", default=TARGET_CURRENCY)
    args = parser.parse_args()

    base_currency = args.base_currency.upper()

    file_name = args.dataset if args.dataset.endswith(".xlsx") else f"{args.dataset}.xlsx"
    file_path = f"./{BASE_DIR}/{DATASET_DIR}/{base_currency}/{file_name}"

    main_df = load_excel(file_path)
    if main_df is None:
        print(f"No xlsx was found in path {file_path}")
        return 

    target_currency_list = ["EUR","JPY","CNY","AUD","CAD","HKD","KWR", "TWD"]
    target_currency_list = [c for c in target_currency_list if c in main_df.columns]
    target_df_with_index = main_df[['timestamp'] + target_currency_list]
    target_df_without_index = main_df[target_currency_list]
    
    fig1 = trend_chart(target_df_with_index, title = "First Chart", showlegend = True)
    fig2 = volatility_barchart(target_df_with_index, title = "Second Chart", showlegend = False)
    fig3 = daily_return_chart(target_df_with_index, title = "Third Chart", showlegend = False)
    fig4 = normalized_index_chart(target_df_with_index, title = "Fourth Chart", showlegend = False)
    fig5 = correlation_heatmap(target_df_without_index, title = "Fith Chart", showlegend = False)
    px_dashboard = dashboard(row = 2, col = 3, figures = [fig1, fig2, fig3, fig4, fig5], keep_first_legend=True)
    
    px_dashboard.show()
    
    


if __name__ == "__main__":
    main()