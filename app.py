"""Main Application File"""

import dash
from dash import Output, Input, dcc, html
from appconfig import appconfig

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for Python.
    """
        ),
        dcc.Input(id="input-text", value="initial value", type="text"),
        html.Div(id="output-text"),
    ]
)


# Define callback to update the output text
@app.callback(
    Output(component_id="output-text", component_property="children"),
    [Input(component_id="input-text", component_property="value")],
)
def update_output_div(input_value):
    return f"You've entered: {input_value} and {appconfig.DASH_APP.APP_TITLE}"


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
