from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import numpy as np
from src.currency.utils.io_utils import load_excel
from src.currency.visualization.components.px_line import line_chart
from src.currency.visualization.components.px_bar import bar_chart
from src.currency.visualization.components.px_heatmap import heatmap
from src.currency.visualization.dashboard import dashboard

DROPDOWN_MENU_LIST = ['TWD', 'JPY', 'USD']

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
    return bar_chart(df, method_apply = apply, **kwargs)


def correlation_heatmap(df: pd.DataFrame, **kwargs):
    apply = lambda df : df.pct_change().dropna().corr()
    return heatmap(df, method_apply = apply, **kwargs)
    

app = Dash()

app.layout = [
    html.H1(children = "Title of Dash App.", style = {'textAlign' : "center"}),
    dcc.Dropdown(DROPDOWN_MENU_LIST, 'TWD', id = 'dropdown-selection'),
    dcc.Graph(id = 'graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    
    df_path = f'./data/proccessed/{value}/dataset_historical_currency-proccess.xlsx'

    main_df = load_excel(df_path)
    target_currency_list = ["EUR","JPY","CNY","AUD","CAD","HKD","KWR", "TWD"]
    target_currency_list = [c for c in target_currency_list if c in main_df.columns and c != value]
    target_df_with_index = main_df[['timestamp'] + target_currency_list]
    target_df_without_index = main_df[target_currency_list]
    
    fig1 = trend_chart(target_df_with_index, title = "First Chart", showlegend = True)
    fig2 = volatility_barchart(target_df_without_index, title = "Second Chart", showlegend = False)
    fig3 = daily_return_chart(target_df_with_index, title = "Third Chart", showlegend = False)
    fig4 = normalized_index_chart(target_df_with_index, title = "Fourth Chart", showlegend = False)
    fig5 = correlation_heatmap(target_df_without_index, title = "Fith Chart", showlegend = False)
    px_dashboard = dashboard(row = 2, col = 3, figures = [fig1, fig2, fig3, fig4, fig5], keep_first_legend=True)
    
    return px_dashboard


if __name__ == '__main__':
    app.run()