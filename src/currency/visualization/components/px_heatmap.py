import plotly.express as px
import pandas as pd

def heatmap(
        df: pd.DataFrame,
        method_apply = None,
        figure_params: dict = {},
        **kwargs
        ):
    
    target_df = df.copy()

    if method_apply:
        if not callable(method_apply):
            raise TypeError("methodApply must be a callable function that accepts a DataFrame.")
        target_df = method_apply(target_df)

    fig = px.imshow(
        target_df,
        text_auto = figure_params.get('text_auto', True),
        aspect = figure_params.get("aspect", "auto"),
        color_continuous_scale = figure_params.get("color_continuous_scale", "RdBu_r"),
        title = figure_params.get("title", "Heatmap"),
        labels = dict(color=figure_params.get("label_name", "Heatmap Label")),
        zmin= figure_params.get("zmin", -1), zmax = figure_params.get("zmax", 1)
    )
    fig.update_layout(
        xaxis_title=figure_params.get("xaxis_title", "Currency"),
        yaxis_title=figure_params.get("yaxis_title", "Currency"),
        showlegend = figure_params.get("showlegend", True),
    )
    fig.update_coloraxes(showscale=figure_params.get("showscale", False))

    return fig