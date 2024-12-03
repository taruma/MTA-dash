"""Main Application File"""

import dash
from dash import Output, Input, State, dcc, _dash_renderer
from string import Template
from appconfig import appconfig
import plotly.graph_objects as go
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import pyfigure
import pylayout
import pyfunc
import pylayoutfunc

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
mta_daily_drop = 1 - (mta_daily_recovery / 100)
mta_data = pyfunc.mta_dict

for mode in mta_data:
    mta_data[mode]["data_ridership"] = mta_daily_ridership[
        mta_data[mode]["ridership_column"]
    ]
    mta_data[mode]["data_recovery"] = mta_daily_recovery[
        mta_data[mode]["recovery_column"]
    ]
    mta_data[mode]["data_drop"] = mta_daily_drop[mta_data[mode]["recovery_column"]]


# LAYOUT

app.layout = pylayout.appshell_layout

# CALLBACKS


@app.callback(
    Output(component_id="plot-mta-ridership-recovery", component_property="figure"),
    Output("div-cards-total-ridership", "children"),
    Output("div-cards-highest-recovery", "children"),
    [
        Input("radiogroup-resample", "value"),
        Input("date-picker-start", "value"),
        Input("date-picker-end", "value"),
        Input("multi-select-transportation", "value"),
        Input("check-disable-ridership", "checked"),
        Input("check-disable-drop", "checked"),
    ],
)
def update_figure_cards(
    selected_time_frequency,
    start_date,
    start_end,
    selected_modes,
    disable_ridership,
    disable_drop,
):
    """Update the figure and cards."""

    selected_modes = mta_data.keys() if not selected_modes else selected_modes

    figure = pyfigure.generate_ridership_recovery(
        mta_data,
        selected_modes,
        start_date,
        start_end,
        selected_time_frequency,
        disable_ridership,
        disable_drop,
    )

    ridership_cards = pylayoutfunc.generate_layout_card_total_ridership(
        mta_data, selected_modes, start_date, start_end
    )

    recovery_cards = pylayoutfunc.generate_layout_card_highest_recovery(
        mta_data, selected_modes, start_date, start_end, selected_time_frequency
    )

    return figure, ridership_cards, recovery_cards


@app.callback(
    Output(component_id="insight-text", component_property="children"),
    [
        Input("button-llm", "n_clicks"),
        State("plot-mta-ridership-recovery", "figure"),
        State("llm-context-system", "value"),
        State("llm-context-project", "value"),
        State("llm-context-stat", "value"),
        State("llm-question", "value"),
        State("multi-select-transportation", "value"),
        State("date-picker-start", "value"),
        State("date-picker-end", "value"),
        State("radiogroup-resample", "value"),
        State("llm-model", "value"),
        State("llm-api-key", "value"),
    ],
    prevent_initial_call=True,
)
def update_insight(
    _,
    fig,
    system_prompt,
    project_overview,
    context_plot_stats,
    user_question,
    selected_mta,
    start_date,
    end_date,
    time_frequency,
    llm_models,
    llm_api_key,
):
    """Generate insight using OpenAI's Language Model API."""

    from datetime import datetime
    import pandas as pd

    template_plot_stats = Template(context_plot_stats)

    # Calculation

    selected_mta_label = []
    data_ridership = []
    data_recovery = []
    for mode in selected_mta:
        selected_mta_label.append(mta_data[mode]["label"])
        data_ridership.append(
            mta_data[mode]["data_ridership"].resample(time_frequency).sum()
        )
        data_recovery.append(
            mta_data[mode]["data_recovery"].resample(time_frequency).mean()
        )

    data_ridership = pd.concat(data_ridership, axis=1)
    data_recovery = pd.concat(data_recovery, axis=1)

    selected_mta_total_ridership = data_ridership.sum()
    selected_mta_ridership_describe = data_ridership.describe()
    selected_mta_recovery_describe = data_recovery.describe()

    selected_mta_label = ", ".join(selected_mta_label)
    start_date = datetime.strptime(start_date, "%Y-%m-%d").strftime("%B %d, %Y")
    end_date = datetime.strptime(end_date, "%Y-%m-%d").strftime("%B %d, %Y")
    time_frequency_label = pyfunc.TIME_FREQUENCY_DICT[time_frequency]

    context_plot_stats = template_plot_stats.substitute(
        selected_mta_label=selected_mta_label,
        start_date=start_date,
        end_date=end_date,
        time_frequency=time_frequency_label,
        selected_mta_total_ridership=selected_mta_total_ridership,
        selected_mta_ridership_describe=selected_mta_ridership_describe,
        selected_mta_recovery_describe=selected_mta_recovery_describe,
    )

    figure = pyfunc.fig_to_base64(go.Figure(fig))

    insight = pyfunc.generate_insight(
        system_prompt,
        project_overview,
        context_plot_stats,
        user_question,
        figure,
        model=llm_models,
        llm_api_key=llm_api_key,
    )

    # return dcc.Textarea("hello")
    return dcc.Markdown(insight)


@app.callback(
    Output("modal-llm-setting", "opened"),
    Input("modal-llm-setting-button", "n_clicks"),
    Input("modal-llm-setting-close-button", "n_clicks"),
    State("modal-llm-setting", "opened"),
    prevent_initial_call=True,
)
def modal_llm_setting(_1, _2, opened):
    return not opened


@app.callback(
    Output("modal-llm-context", "opened"),
    Input("modal-llm-context-button", "n_clicks"),
    Input("modal-llm-context-close-button", "n_clicks"),
    State("modal-llm-context", "opened"),
    prevent_initial_call=True,
)
def modal_llm_context(_1, _2, opened):
    return not opened


# Run the app
if __name__ == "__main__":
    app.run_server(debug=DEBUG_MODE)
