
import plotly.express as px
import pandas as pd

def line_chart(
        df: pd.DataFrame, 
        method_apply = None,
        index_column: str = 'timestamp',
        melt: bool = False,
        figure_params: dict = {},
        **kwargs
        ):
    
    if index_column not in df.columns:
        raise ValueError(f"Index Column '{index_column}' not found in DataFrame.")
    
    target_df = df.copy()

    if method_apply:
        if not callable(method_apply):
            raise TypeError("methodApply must be a callable function that accepts a DataFrame.")
        transformed_part = method_apply(df.drop(columns=[index_column]))
        target_df = pd.concat([target_df[[index_column]], transformed_part], axis=1)

    target_df[index_column] = pd.to_datetime(target_df[index_column], unit='s')

    var_name = figure_params.get("var_name", "currency")
    value_name = figure_params.get("value_name", "daily_return")
    title = figure_params.get("title", f"{var_name.capitalize()} Trend Chart")

    # auto-format labels unless provided
    default_labels = {
        var_name: var_name.replace("_", " ").title(),
        value_name : value_name.replace("_", " ").title(),
        index_column : index_column.replace("_", " ").title()
    }

    labels = figure_params.get('labels', default_labels)
    log_y = figure_params.get('log_y', False)

    if melt:
        target_df = pd.melt(target_df,
                            id_vars=index_column,
                            var_name=var_name,
                            value_name=value_name)

    fig = px.line(
        target_df,
        x = index_column,
        y = value_name,
        color = var_name,
        title = title,
        labels = labels,
        log_y = log_y
    ) if melt else px.line(
        target_df,
        x = index_column,
        y = value_name,
        title = title,
        labels = labels,
        log_y = log_y
    )

    fig.update_layout(
        hovermode = figure_params.get("hovermode", "x unified"),
        template = figure_params.get("template", "plotly_white"),
        showlegend = figure_params.get("showlegend", True),
        xaxis_title = labels.get(index_column, index_column),
        yaxis_title = labels.get(value_name, value_name),
        legend_title_text = labels.get(var_name, var_name) if melt else None
    )

    return fig
