"""Layout Module for Dash App"""

from datetime import date
from dash import dcc, html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
from appconfig import appconfig, projectconfig
import pyfigure
import pyfunc

# APPCONFIG
main_title_text = appconfig.dash.title
main_subtitle_text = appconfig.dash.subtitle

# MAIN ========================================

# TITLE
main_title = dmc.Center(dmc.Title(main_title_text, order=1, mt="xl"))
main_subtitle = dmc.Center(
    dmc.Text(main_subtitle_text, c="dimmed", style={"fontSize": "1.2rem"})
)

# LINKS

github_link = dmc.Anchor(
    DashIconify(icon="mdi:github", width=25),
    href=appconfig.repository.github_url,
    target="_blank",
)

version_app = dmc.Badge(
    f"{projectconfig.project.version}",
    # variant="dot",
    size="md",
)

# SHORT DESCRIPTION

DESRIPTION = pyfunc.read_text_file("text/app_description.md")

short_description = dmc.Center(
    dmc.Paper(dcc.Markdown(DESRIPTION), shadow="lg", mt="md", w="80%", pt="md", px="lg")
)

# PLOT-1
plot_title = dmc.Title("MTA Ridership Trends", order=2, my="md", ta="center")
plot_description_text = pyfunc.read_text_file("text/app_plot1_description.md")

plot_description = dmc.Text(
    dcc.Markdown(plot_description_text),
    ta="center",
    px="xl",
)
plot_mta_ridership_trends = dcc.Graph(
    id="plot-mta-ridership-recovery", figure=pyfigure.generate_empty_figure("empty")
)

# SELECT DATE

date_picker_start = dmc.DatePickerInput(
    id="date-picker-start",
    label="Start Date",
    minDate=date(2020, 3, 1),
    maxDate=date(2024, 10, 31),
    value=date(2020, 3, 1),
    w=150,
)

date_picker_end = dmc.DatePickerInput(
    id="date-picker-end",
    label="End Date",
    minDate=date(2020, 3, 1),
    maxDate=date(2024, 10, 31),
    value=date(2024, 10, 31),
    w=150,
)

# MULTI SELECT

multi_select = dmc.MultiSelect(
    label="Select MTA Services:",
    placeholder="Select one or more...",
    id="multi-select-transportation",
    value=["lirr", "mnr"],
    data=[
        {"value": value, "label": f"{emoji} {label}"}
        for value, label, emoji in zip(
            pyfunc.TRANSPORTATION_MODES,
            pyfunc.TRANSPORTATION_NAMES,
            pyfunc.TRANSPORTATION_EMOJI,
        )
    ],
    clearable=True,
    searchable=True,
    leftSectionPointerEvents="none",
    leftSection=DashIconify(icon="material-symbols:transit-ticket-outline"),
    # w=750,
)

# SHOW RIDERSHIP/RECOVERY/DROP ONLY
check_ridership = dmc.Checkbox(
    id="check-disable-ridership", label="Hide Ridership", checked=False, size="sm"
)

check_drop = dmc.Checkbox(
    id="check-disable-drop", label="Hide Drop", checked=False
)

# SELECT RESAMPLE PERIOD
radio_data = [
    ["D", "Daily"],
    ["W", "Weekly"],
    ["ME", "Monthly"],
    ["YE", "Yearly"],
]

resample_period_radio = dmc.RadioGroup(
    children=dmc.Group(
        [dmc.Radio(label, value=value) for value, label in radio_data], my=10
    ),
    id="radiogroup-resample",
    value="W",
    label="Data Aggregation",
    size="sm",
    mb="sm",
)

# LLM

plot1_llm_title = dmc.Title("Insight (with LLM)", order=3, my="md", size="md")
llm_model = dmc.TextInput(
    id="llm-model",
    label="LLM Model (provider:model-name)",
    value="openai:gpt-4o-mini",
    placeholder="Enter model name with this format provider:model-name",
    w=250,
)
llm_api_key = dmc.PasswordInput(
    label="OpenAI API Key",
    placeholder="sk-.....",
    id="llm-api-key",
    w=300,
)

placeholder_insight = pyfunc.read_text_file("text/app_plot1_insight.md")
plot1_insight = dmc.Center(
    dmc.Paper(
        dcc.Markdown(placeholder_insight),
        shadow="lg",
        mt="md",
        w="90%",
        pt="md",
        px="lg",
        id="insight-text",
    )
)

loading_plot1_insight = dcc.Loading(
    id="loading-plot1-insight",
    children=plot1_insight,
    type="default",
)


# FOOTER

note_footer = dmc.Center(
    dmc.Text(
        [
            "This app was created as a submission for the ",
            dmc.Anchor(
                "Plotly & Maven Analytics Holiday Season App Challenge",
                href="https://community.plotly.com/t/holiday-season-app-challenge-nyc-mta/88389",
                target="_blank",
                style={"fontSize": "0.8rem"},
            ),
            ".",
        ],
        c="dimmed",
        style={"fontSize": "0.8rem"},
    )
)

# APPSHELL ====================================

appshell_main = dmc.AppShellMain(
    [
        main_title,
        main_subtitle,
        dmc.Group(
            [
                version_app,
                github_link,
            ],
            justify="center",
            my="sm",
        ),
        dmc.Divider(variant="solid"),
        dmc.Center(short_description),
        dmc.Center(plot_title),
        plot_description,
        dmc.Group(
            [multi_select, date_picker_start, date_picker_end, resample_period_radio],
            justify="center",
            align="buttom",
        ),
        plot_mta_ridership_trends,
        dmc.Space(h="sm"),
        dmc.Text("Additional Setting", c="dimmed", size="md", fw=500, ta="center"),
        dmc.Space(h="sm"),
        dmc.Flex(
            [
                check_ridership,
                check_drop,
            ],
            justify="center",
            align="center",
            gap="md",
        ),
        dmc.Space(h="sm"),
        dmc.Text("At a Glance Stats", c="dimmed", size="md", fw=500, ta="center"),
        html.Div(id="div-cards-total-ridership"),
        dmc.Space(h="sm"),
        dmc.Center(plot1_llm_title),
        dmc.Group(
            [
                llm_model,
                llm_api_key,
                dmc.Button("Generate Insight", id="button-llm", variant="gradient"),
            ],
            justify="center",
            align="flex-end",
        ),
        loading_plot1_insight,
        dmc.Space(h="xl"),
        dmc.Divider(variant="solid"),
        dmc.Space(h="xl"),
        note_footer,
    ]
)


# APPSHELL LAYOUT =============================

appshell_layout = dmc.MantineProvider(
    dmc.AppShell(
        [
            appshell_main,
        ],
        padding="xl",
    )
)
