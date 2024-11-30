"""MODULE FOR GENERATE FIGURE"""

from itertools import cycle, islice
import plotly.graph_objects as go

# import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
from appconfig import appconfig
from pytemplate import mytemplate
import pyfunc


def generate_watermark(subplot_number: int = 1) -> dict:
    """GENERATE DICT WATERMARK FOR SUBPLOTS"""

    subplot_number = "" if subplot_number == 1 else subplot_number
    return {
        "source": appconfig.template.watermark_source,
        "xref": f"x{subplot_number} domain",
        "yref": f"y{subplot_number} domain",
        "x": 0.5,
        "y": 0.5,
        "sizex": 0.5,
        "sizey": 0.5,
        "xanchor": "center",
        "yanchor": "middle",
        "name": "watermark",
        "layer": "below",
        "opacity": 0.2,
    }


def generate_empty_figure(
    text: str = "", size: int = 40, margin_all: int = 0, height: int = 450
) -> go.Figure:
    """GENERATE FIGURE EMPTY"""

    data = [{"x": [], "y": []}]

    layout = go.Layout(
        title={"text": "", "x": 0.5},
        xaxis={
            "title": "",
            "showgrid": False,
            "showticklabels": False,
            "zeroline": False,
        },
        yaxis={
            "title": "",
            "showgrid": False,
            "showticklabels": False,
            "zeroline": False,
        },
        margin={"t": 0, "l": margin_all, "r": margin_all, "b": 0},
        annotations=[
            {
                "name": "text",
                "text": f"<i>{text}</i>",
                "opacity": 0.3,
                "font_size": size,
                "xref": "x domain",
                "yref": "y domain",
                "x": 0.5,
                "y": 0.5,
                "showarrow": False,
            }
        ],
        height=height,
    )

    return go.Figure(data, layout)


def generate_ridership_recovery(
    mta_daily_ridership: pd.DataFrame,
    mta_daily_recovery: pd.DataFrame,
    resample_period: str = None,
    date_start: str = None,
    date_end: str = None,
    modes: list = None,
) -> go.Figure:
    """GENERATE FIGURE RIDERSHIP RECOVERY"""

    resample_period = "W" if resample_period is None else resample_period
    date_start = mta_daily_ridership.index.min() if date_start is None else date_start
    date_end = mta_daily_ridership.index.max() if date_end is None else date_end
    modes = pyfunc.TRANSPORTATION_MODES if (modes is None) or (not modes) else modes

    mta_daily_ridership = mta_daily_ridership.loc[date_start:date_end]
    mta_daily_recovery = mta_daily_recovery.loc[date_start:date_end]

    transportation_label = list(zip(pyfunc.TRANSPORTATION_MODES, pyfunc.TRANSPORTATION_NAMES, pyfunc.TRANSPORTATION_EMOJI))

    selected_transportation_label = [
        (mode, name, emoji)
        for mode, name, emoji in transportation_label if mode in modes
    ]

    colorway = mytemplate.layout.colorway
    colors = list(islice(cycle(colorway), len(selected_transportation_label)))

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    is_above_zero = False

    for counter, (mode, mode_name, emoji) in enumerate(
        selected_transportation_label
    ):
        is_legend_visible = True # if counter == 0 else "legendonly"

        ridership_column = [
            col for col in mta_daily_ridership.columns if col.startswith(mode)
        ][0]
        recovery_column = [
            col for col in mta_daily_recovery.columns if col.startswith(mode)
        ][0]

        selected_ridership = (
            mta_daily_ridership[ridership_column].resample(resample_period).sum()
        )
        selected_recovery = 1 - (
            mta_daily_recovery[recovery_column].resample(resample_period).mean()
        ) / 100

        is_above_zero = is_above_zero or (selected_recovery < 0).any()

        ridership_trace = go.Scatter(
            x=selected_ridership.index,
            y=selected_ridership.values,
            name=f"{mode}_ridership",
            legendgroup=mode,
            legendgrouptitle_text=f"{emoji} {mode_name}",
            line_color=colors[counter],
            line_width=3,
            hovertemplate="%{y}",
            visible=is_legend_visible,
        )

        recovery_trace = go.Scatter(
            x=selected_recovery.index,
            y=selected_recovery.values,
            name=f"{mode}_drop",
            yaxis="y2",
            legendgroup=mode,
            legendgrouptitle_text=f"{emoji} {mode_name}",
            line_dash="dot",
            line_color=colors[counter],
            line_width=2,
            visible=is_legend_visible,
        )

        fig.add_trace(ridership_trace)
        fig.add_trace(recovery_trace)

    fig.update_layout(
        xaxis=dict(title="Date"),
        yaxis=dict(
            title="Estimated Ridership",
            # tickformat=".3s",
            gridwidth=2,
            hoverformat=".3s",
        ),
        yaxis2=dict(
            title="Percentage Drop from Pre-Pandemic (%)",
            # autorange="reversed",
            hoverformat=".2%",
            tickformat=".0%",  # https://observablehq.com/@d3/d3-format?collection=@d3/d3-format
            griddash="dashdot",
        ),
        margin={"t": 30, "l": 10, "r": 10, "b": 10},
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
        ),
    )

    fig.add_hline(y=0, line_dash="dash",line_color=colors[0], line_width=2, yref="y2")

    if is_above_zero:
        fig.add_annotation(
            text="<i><b>Beyond Recovery</b></i>",
            showarrow=False,
            x=1,
            xref="x domain",
            xanchor="right",
            y=0,
            yref="y2",
            yanchor="top",

        )

    return fig
