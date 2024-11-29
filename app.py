"""Main Application File"""

import dash
from dash import Output, Input, dcc, html
from appconfig import appconfig
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from pylayout import appshell_layout

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
        dmc.styles.ALL,
        dbc.icons.FONT_AWESOME
    ],
    title=PAGE_TITLE,
    # meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True,
)
server = app.server

app.layout = appshell_layout

# CALLBACKS

# Define callback to update the output text
@app.callback(
    Output(component_id="output-text", component_property="children"),
    [Input(component_id="input-text", component_property="value")],
)
def update_output_div(input_value):
    return f"You've entered: {input_value} and {appconfig.dash.title}"


# Run the app
if __name__ == "__main__":
    app.run_server(debug=DEBUG_MODE)
