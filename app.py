"""Main Application File"""

import dash
from dash import Output, Input, State, dcc, _dash_renderer
from appconfig import appconfig
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import pyfigure
import pylayout
import pyfunc
import plotly.graph_objects as go
_dash_renderer._set_react_version("18.2.0")

# Dash app configuration
APP_TITLE = appconfig.dash.title
PAGE_TITLE = appconfig.dash.page_title
LOADING_MESSAGE = appconfig.dash.loading_message
DEBUG_MODE = appconfig.dash.debug
THEME = appconfig.template.theme

# Initialize the Dash app
app = dash.Dash(
    name=APP_TITLE,
    external_stylesheets=[
        getattr(dbc.themes, THEME),
        # dmc.styles.ALL,
        dmc.styles.DATES,
        dbc.icons.FONT_AWESOME,
    ],
    title=PAGE_TITLE,
    # meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=False,
)
server = app.server

# Load data

mta_daily = pyfunc.get_mta_daily()
mta_daily_ridership = pyfunc.get_mta_ridership_recovery(mta_daily, is_ridership=True)
mta_daily_recovery = pyfunc.get_mta_ridership_recovery(mta_daily, is_ridership=False)


# LAYOUT

app.layout = pylayout.appshell_layout

# CALLBACKS


# Define callback to update the output text
@app.callback(
    Output(component_id="plot-mta-ridership-recovery", component_property="figure"),
    [
        Input(component_id="radiogroup-resample", component_property="value"),
        Input(component_id="date-picker-start", component_property="value"),
        Input(component_id="date-picker-end", component_property="value"),
        Input(component_id="multi-select-transportation", component_property="value"),
    ],
)
def update_output_div(resample_period, date_start, date_end, transportation_modes):
    return pyfigure.generate_ridership_recovery(
        mta_daily_ridership,
        mta_daily_recovery,
        resample_period,
        date_start,
        date_end,
        transportation_modes,
    )


@app.callback(
    Output(component_id="insight-text", component_property="children"),
    [
        Input("button-llm", "n_clicks"),
        State("plot-mta-ridership-recovery", "figure"),
        State("llm-model", "value"),
        State("llm-api-key", "value"),
        State("date-picker-start", "value"),
        State("date-picker-end", "value"),
        State("radiogroup-resample", "value"),
    ],
    prevent_initial_call=True,
)
def update_insight(
    _, fig, llm_models, llm_api_key, start_date, end_date, resample_period
):
    system_prompt = pyfunc.read_text_file("text/system_prompt.md")
    context_overview = pyfunc.read_text_file("text/context_overview.md")

    figure = pyfunc.fig_to_base64(go.Figure(fig))

    insight = pyfunc.generate_insight(
        system_prompt,
        context_overview,
        figure,
        model=llm_models,
        llm_api_key=llm_api_key,
        start_date=start_date,
        end_date=end_date,
        resample_period=resample_period
    )

    return dcc.Markdown(insight)


# Run the app
if __name__ == "__main__":
    app.run_server(debug=DEBUG_MODE)
