"""Main Application File"""

import dash
from dash import Output, Input, dcc, html
from appconfig import appconfig
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

# Dash app configuration
APP_TITLE = appconfig.dash.title
PAGE_TITLE = appconfig.dash.page_title
LOADING_MESSAGE = appconfig.dash.loading_message
DEBUG_MODE = appconfig.dash.debug

# Bootstrap Theme
THEME = appconfig.template.theme

# Initialize the Dash app
app = dash.Dash(
    name=APP_TITLE,
    external_stylesheets=[
        getattr(dbc.themes, THEME),
        dmc.styles.ALL,
        dbc.icons.FONT_AWESOME,
    ],
    title=PAGE_TITLE,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True,
)
server = app.server

# Define the layout of the appub
layout_header = dbc.Row(
    [
        html.H1("Metro Track Dash"),
        html.Div(
            """
                    Dash: A web application framework for Python.
                    """
        ),
    ],
    class_name="text-center mb-3",
)

layout_footer = dmc.AppShellFooter(
    withBorder=True,
    children=[
        dmc.Group(
            [
                dcc.Link("Contact", href="/"),
                dcc.Link("Privacy", href="/"),
                dcc.Link("Blog", href="/"),
                dcc.Link("Store", href="/"),
                dcc.Link("Careers", href="/"),
            ],
            className="footer-center",
        ),
        dmc.Group(
            [
                dcc.Link(
                    dmc.Avatar(
                        html.I(className="fa-brands fa-twitter fa-fw fa-lg"),
                        radius="xl",
                    ),
                    href="/",
                ),
                dcc.Link(
                    dmc.Avatar(
                        html.I(className="fa-brands fa-instagram fa-fw fa-lg"),
                        radius="xl",
                    ),
                    href="/",
                ),
                dcc.Link(
                    dmc.Avatar(
                        html.I(className="fa-brands fa-youtube fa-fw fa-lg"),
                        radius="xl",
                    ),
                    href="/",
                ),
            ],
            className="footer-right",
        ),
    ],
)

appshell_test = dmc.AppShell(
    [
        dmc.AppShellHeader("Header", px=25),
        dmc.AppShellFooter(children=[layout_footer]),

        dmc.AppShellMain(children=[layout_header]),
    ],
    header={"height": 70},
    padding="xl",
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    aside={
        "width": 300,
        "breakpoint": "xl",
        "collapsed": {"desktop": False, "mobile": True},
    },
)

app.layout = dmc.MantineProvider(
    [
        # layout_header,
        appshell_test,
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             dbc.Input(
        #                 id="input-text",
        #                 value="initial value",
        #                 type="text",
        #             ),
        #             width=3,
        #             class_name="mx-auto",
        #         ),
        #     ]
        # ),
        # dbc.Row(
        #     [
        #         html.Div(id="output-text"),
        #         dmc.Alert(
        #             "Hi from Dash Mantine Components. You can create some great looking dashboards using me!",
        #             title="Welcome!",
        #             color="violet",
        #             className="w-80 mx-auto",
        #         ),
        #     ],
        #     # class_name="mt-3",
        # ),
    ],
)


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
