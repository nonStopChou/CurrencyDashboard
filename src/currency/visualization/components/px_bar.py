import plotly.express as px
import pandas as pd
import numpy as np


def bar_chart(df: pd.DataFrame,
              method_apply = None,
              figure_params: dict = {},
              **kwargs
              ):
    
    target_df = df.copy()

    if method_apply:
        if not callable(method_apply):
            raise TypeError("methodApply must be a callable function that accepts a DataFrame.")
        target_df = method_apply(target_df)
    
    value_name = figure_params.get("value_name", "Volatility (%)")
    title = figure_params.get("title", "Volatility Ranking.")
    color_scale = figure_params.get("color_scale", "Viridis")
    orientation = figure_params.get('orientation', 'h')

    label_name = figure_params.get("label_name", "Currency").replace("_", " ").title()

    volatility_df = pd.DataFrame(
        {
            label_name : target_df.index,
            value_name : target_df.values
        }
    )

    if volatility_df.empty:
        raise ValueError("No valid volatility data found (check numeric columns or missing values).")

    if orientation == 'h':
        x_axis, y_axis = value_name, label_name
    else:
        x_axis, y_axis = label_name, value_name
    
    fig = px.bar(
        volatility_df,
        x = x_axis,
        y = y_axis,
        title = title,
        text = value_name,
        color = value_name,
        color_continuous_scale = color_scale,
        orientation = orientation
    )

    fig.update_coloraxes(showscale=False)
    fig.update_yaxes(categoryorder='total ascending')
    
    fig.update_layout(
        showlegend = figure_params.get("showlegend", True),
    )


    return fig 
