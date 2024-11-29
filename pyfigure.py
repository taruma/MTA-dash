"""MODULE FOR GENERATE FIGURE"""


import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from appconfig import appconfig

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