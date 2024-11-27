"""
PLOTLY TEMPLATE BASED ON THEME
version: v1.2.0 (modified from taruma/anfrek)
"""

from plotly import colors
from dash_bootstrap_templates import load_figure_template
import plotly.io as pio
from appconfig import appconfig

load_figure_template(appconfig.template.theme.lower())
mytemplate = pio.templates[pio.templates.default]

# VARS
_FONT_FAMILY = mytemplate.layout.font.family
FONT_COLOR_TUPLE = colors.hex_to_rgb(mytemplate.layout.font.color)
_red, _green, _blue = FONT_COLOR_TUPLE
FONT_COLOR_RGB_ALPHA = f"rgba({_red},{_green},{_blue},0.2)"

# LAYOUT
mytemplate.layout.images = [
    {
        "source": appconfig.template.watermark_source,
        "xref": "x domain",
        "yref": "y domain",
        "x": 0.5,
        "y": 0.5,
        "sizex": 0.5,
        "sizey": 0.5,
        "xanchor": "center",
        "yanchor": "middle",
        "name": "watermark-taruma",
        "layer": "below",
        "opacity": 0.2,
    }
]

# GENERAL

mytemplate.layout.hovermode = "x"
mytemplate.layout.margin.t = 80
mytemplate.layout.margin.b = 35
mytemplate.layout.margin.l = 55  
mytemplate.layout.margin.r = 55
mytemplate.layout.margin.pad = 0
mytemplate.layout.paper_bgcolor = mytemplate.layout.plot_bgcolor

# LEGEND
LEGEND_FONT_SIZE = 15
mytemplate.layout.showlegend = True
mytemplate.layout.legend.font.size = LEGEND_FONT_SIZE
mytemplate.layout.legend.groupclick = "toggleitem"


# MODEBAR
mytemplate.layout.modebar.activecolor = "blue"
mytemplate.layout.modebar.add = (
    "hoverclosest hovercompare v1hovermode togglehover drawrect eraseshape".split()
)
mytemplate.layout.modebar.bgcolor = "rgba(0,0,0,0)"
mytemplate.layout.modebar.color = "rgba(0,0,0,0.6)"

# NEWSHAPE
mytemplate.layout.newshape.line.color = "red"
mytemplate.layout.newshape.line.width = 3

# HOVERLABEL
mytemplate.layout.hoverlabel.font.family = _FONT_FAMILY

# TITLE
mytemplate.layout.title.pad = dict(b=10, l=0, r=0, t=0)
mytemplate.layout.title.x = 0
mytemplate.layout.title.xref = "paper"
mytemplate.layout.title.y = 1
mytemplate.layout.title.yref = "paper"
mytemplate.layout.title.yanchor = "bottom"
mytemplate.layout.title.font.size = 35

# XAXIS
_XAXIS_GRIDCOLOR = "black" # .layout.xaxis.gridcolor
_XAXIS_LINEWIDTH = 1
_XAXIS_TITLE_FONT_SIZE = 20
_XAXIS_TITLE_STANDOFF = 20
mytemplate.layout.xaxis.mirror = True
mytemplate.layout.xaxis.showline = True
mytemplate.layout.xaxis.linewidth = _XAXIS_LINEWIDTH
mytemplate.layout.xaxis.linecolor = _XAXIS_GRIDCOLOR
mytemplate.layout.xaxis.spikecolor = _XAXIS_GRIDCOLOR
mytemplate.layout.xaxis.gridcolor = FONT_COLOR_RGB_ALPHA
mytemplate.layout.xaxis.gridwidth = _XAXIS_LINEWIDTH
mytemplate.layout.xaxis.title.text = "<b>PLACEHOLDER XAXIS</b>"
mytemplate.layout.xaxis.title.font.size = _XAXIS_TITLE_FONT_SIZE
mytemplate.layout.xaxis.title.standoff = _XAXIS_TITLE_STANDOFF
mytemplate.layout.xaxis.spikethickness = 1
mytemplate.layout.xaxis.spikemode = "across"
mytemplate.layout.xaxis.spikedash = "solid"


# YAXIS
_YAXIS_GRIDCOLOR = "black"  # .layout.yaxis.gridcolor
_YAXIS_LINEWIDTH = 1
_YAXIS_TITLE_FONT_SIZE = 20
_YAXIS_TITLE_STANDOFF = 15
mytemplate.layout.yaxis.mirror = True
mytemplate.layout.yaxis.showline = True
mytemplate.layout.yaxis.linewidth = _YAXIS_LINEWIDTH
mytemplate.layout.yaxis.linecolor = _YAXIS_GRIDCOLOR
mytemplate.layout.yaxis.spikecolor = _YAXIS_GRIDCOLOR
mytemplate.layout.yaxis.rangemode = "tozero"
mytemplate.layout.yaxis.gridcolor = FONT_COLOR_RGB_ALPHA
mytemplate.layout.yaxis.gridwidth = _YAXIS_LINEWIDTH
mytemplate.layout.yaxis.title.text = "<b>PLACEHOLDER XAXIS</b>"
mytemplate.layout.yaxis.title.font.size = _YAXIS_TITLE_FONT_SIZE
mytemplate.layout.yaxis.title.standoff = _YAXIS_TITLE_STANDOFF

# SUBPLOTS
# ANNOTATION
mytemplate.layout.annotationdefaults.font.color = mytemplate.layout.font.color
mytemplate.layout.annotationdefaults.font.size = 15


# LAYOUT BAR
mytemplate.layout.barmode = "stack"
mytemplate.layout.bargap = 0

# =============
# PLOT SPECIFIC
# =============

# HEATMAP
mytemplate.data.heatmap[0].textfont.family = _FONT_FAMILY
mytemplate.data.heatmap[0].colorscale = "BlackBody"
mytemplate.data.heatmap[0].colorbar.outlinecolor = "black"
mytemplate.data.heatmap[0].colorbar.outlinewidth = 2
mytemplate.data.heatmap[0].colorbar.ticksuffix = "%"
mytemplate.data.heatmap[0].colorbar.x = 1
mytemplate.data.heatmap[0].colorbar.xpad = 10
mytemplate.data.heatmap[0].colorbar.y = 0.5
mytemplate.data.heatmap[0].colorbar.ypad = 20
