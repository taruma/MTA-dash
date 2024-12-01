"""MODULE FOR GENERATE FIGURE"""

from itertools import cycle, islice
import plotly.graph_objects as go

# import plotly.express as px
from plotly.subplots import make_subplots
from appconfig import appconfig
from pytemplate import mytemplate


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
    mta_data: dict,
    selected_modes: list = None,
    start_date: str = None,
    start_end: str = None,
    time_frequency: str = None,
    disable_ridership: bool = False,
    disable_drop: bool = False,
) -> go.Figure:
    """GENERATE FIGURE RIDERSHIP RECOVERY"""

    colorway = mytemplate.layout.colorway
    colors = list(islice(cycle(colorway), len(selected_modes)))

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    is_surpass_baseline = False

    for counter, mode in enumerate(selected_modes):
        data_ridership = mta_data[mode]["data_ridership"]
        data_drop = mta_data[mode]["data_drop"]

        filtered_ridership = (
            data_ridership.loc[start_date:start_end].resample(time_frequency).sum()
        )
        filtered_drop = (
            data_drop.loc[start_date:start_end].resample(time_frequency).mean()
        )

        is_surpass_baseline = is_surpass_baseline or ((filtered_drop < 0).any())

        ridership_trace = go.Scatter(
            x=filtered_ridership.index,
            y=filtered_ridership.values,
            name=mta_data[mode]["ridership_column"],
            legendgroup=mode,
            legendgrouptitle_text=mta_data[mode]["label"],
            line_color=colors[counter],
            line_width=3,
            hovertemplate="%{y}",
            visible="legendonly" if disable_ridership else True,
        )

        drop_trace = go.Scatter(
            x=filtered_drop.index,
            y=filtered_drop.values,
            name=f"{mode}_drop",  # no "drop_column" in mta_data
            yaxis="y2",
            legendgroup=mode,
            legendgrouptitle_text=mta_data[mode]["label"],
            line_dash="dot",
            line_color=colors[counter],
            line_width=2,
            visible="legendonly" if disable_drop else True,
        )

        fig.add_trace(ridership_trace) 
        fig.add_trace(drop_trace)

    fig.update_layout(
        xaxis=dict(title="Date"),
        yaxis=dict(
            title="Estimated Ridership" if not disable_ridership else "",
            # tickformat=".3s",
            gridwidth=2,
            hoverformat=".3s",
            showgrid=False if disable_ridership else True,
            showticklabels=False if disable_ridership else True,
        ),
        yaxis2=dict(
            title="Percentage Drop from Pre-Pandemic (%)" if not disable_drop else "",
            # autorange="reversed",
            hoverformat=".2%",
            tickformat=".0%",  # https://observablehq.com/@d3/d3-format?collection=@d3/d3-format
            griddash="dashdot",
            showgrid=False if disable_drop else True,
            showticklabels=False if disable_drop else True,
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

    if is_surpass_baseline and not disable_drop:
            fig.add_hline(
                y=0, line_dash="dash", line_color=colors[0], line_width=2, yref="y2"
            )
            fig.add_annotation(
                text="<i><b>Surpassing 2019 Levels</b></i>",
                showarrow=False,
                x=1,
                xref="x domain",
                xanchor="right",
                y=0,
                yref="y2",
                yanchor="top",
            )

    return fig
