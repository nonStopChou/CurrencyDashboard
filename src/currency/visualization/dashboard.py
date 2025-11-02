from plotly.subplots import make_subplots

def dashboard(row: int, col: int, figures: list, height:int = 900, width:int = 1600, 
              dashboard_param: dict = {}, figure_param: dict = {}, **kwargs):

    vertical_spacing = kwargs.get("vertical_spacing", 0.15)
    horizontal_spacing = kwargs.get("horizontal_spacing", 0.07)

    figure_all = make_subplots(
        rows = row, cols = col,
        subplot_titles = [
            fig.layout.title.text for fig in figures
        ],
        vertical_spacing = vertical_spacing,
        horizontal_spacing = horizontal_spacing
    )

    flow_direction = figure_param.get("flow", "row")
    row_reversed = figure_param.get("h_order_reverse", False)
    col_reversed = figure_param.get("v_order_reverse", False)
     

    if flow_direction == "row":
        positions = [(r, c) 
            for r in (reversed(range(1, row + 1)) if row_reversed else range(1, row + 1))
            for c in (reversed(range(1, col + 1)) if col_reversed else range(1, col + 1))
        ]
    else: 
        positions = [(r, c) 
            for c in (reversed(range(1, col + 1)) if col_reversed else range(1, col + 1))
            for r in (reversed(range(1, row + 1)) if row_reversed else range(1, row + 1))
        ]
    
    keep_first_legend = kwargs.get("keep_first_legend", False)
    for i, figure in enumerate(figures):
        for trace in figure.data:
            row, col = positions[i]
            
            if keep_first_legend:
                trace.update(showlegend = (i == 0))

            figure_all.add_trace(trace, row = row, col = col)

    
    template = dashboard_param.get("template", "plotly_white")
    showlegend = dashboard_param.get("showlegend", True)
    dashboard_title = dashboard_param.get("title", "Dashboard Title")
    legend_orientation = dashboard_param.get("legend_orientation", "h")
    legend_title = dashboard_param.get("legend_title", "Title")

    figure_all.update_layout(
        height = height, width = width,
        template = template,
        title_text = dashboard_title,
        showlegend = showlegend,
        legend = dict(
            orientation=legend_orientation,       # 水平放在底部
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            title=legend_title
        ),
        margin=dict(l=50, r=150, t=100, b=100)
    )

    colorscale = dashboard_param.get("colorscale", "RdBu_r")
    colorscale_min = dashboard_param.get("colorscale_min", -1)
    colorscale_max = dashboard_param.get("colorscale_max", -1)
    figure_all.update_coloraxes(colorscale=colorscale, cmin=-colorscale_min, cmax=colorscale_max)

    return figure_all


