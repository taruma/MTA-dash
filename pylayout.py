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
main_title = dmc.Text(
    main_title_text, mt="xl", ta="center", size="2rem", fw=700, mb="xs"
)
main_subtitle = dmc.Text(main_subtitle_text, c="dimmed", size="1.2rem", ta="center")


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
plot_title = dmc.Text(
    "MTA Ridership Trends", my="md", ta="center", size="1.5rem", fw=600
)
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
    searchable=False,
    leftSectionPointerEvents="none",
    leftSection=DashIconify(icon="material-symbols:transit-ticket-outline"),
    # w=750,
)

# SHOW RIDERSHIP/RECOVERY/DROP ONLY
check_ridership = dmc.Checkbox(
    id="check-disable-ridership", label="Hide Ridership Trend", checked=False, size="sm"
)

check_drop = dmc.Checkbox(
    id="check-disable-drop", label="Hide Percentage Drop Trend", checked=False
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

default_question = pyfunc.read_text_file("text/default_question.md")

llm_question = dmc.Textarea(
    id="llm-question",
    label=dmc.Text("🔍 Uncover Insights with 🤖 LLM", size="lg", fw=600),
    value=default_question,
    description="What do you want to know about the data?",
    w=1200,
    size="md",
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

# LAYOUT BUTTON

modal_llm_setting = dmc.Modal(
    title=dmc.Text("LLM Settings", size="lg", fw=700),
    id="modal-llm-setting",
    children=[
        dmc.Group(
            [llm_model, llm_api_key],
            justify="flex-start",
            align="flex-end",
            grow=True,
        ),
        dmc.Space(h=20),
        dmc.Group(
            [
                dmc.Button(
                    "Close",
                    color="red",
                    variant="outline",
                    id="modal-llm-setting-close-button",
                )
            ],
            justify="flex-end",
        ),
    ],
    size="lg",
    centered=True,
)


llm_context_system = dmc.Textarea(
    id="llm-context-system",
    label="System Prompt",
    value=pyfunc.read_text_file("text/system_prompt.md"),
    autosize=True,
    minRows=5,
    w=550
)

llm_context_project = dmc.Textarea(
    id="llm-context-project",
    label="Context: Project Overview",
    value=pyfunc.read_text_file("text/project_overview.md"),
    autosize=True,
    minRows=5,
    w=550
)

llm_context_stat = dmc.Textarea(
    id="llm-context-stat",
    label="Context: Statistical & Plot Description",
    autosize=True,
    value=pyfunc.read_text_file("text/context_plot_stat.md"),
    minRows=5,
    w=550
)

modal_llm_context = dmc.Modal(
    title=dmc.Text("LLM Context", size="lg"),
    id="modal-llm-context",
    children=[
        dmc.Group(
            [
                llm_context_system,
                llm_context_project,
                llm_context_stat,
            ],
            justify="center",
            align="flex-start",
            wrap=True,
        ),
        dmc.Space(h=20),
        dmc.Group(
            [
                dmc.Button(
                    "Close",
                    color="red",
                    variant="outline",
                    id="modal-llm-context-close-button",
                ),
            ],
            justify="flex-end",
        ),
    ],
    fullScreen=True,
    centered=True,
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
        dmc.Divider(variant="solid", m="md"),
        plot_title,
        plot_description,
        dmc.Group(
            [multi_select, date_picker_start, date_picker_end, resample_period_radio],
            justify="center",
            align="buttom",
        ),
        plot_mta_ridership_trends,
        dmc.Space(h="sm"),
        dmc.Text("Display Options", c="dimmed", size="md", fw=500, ta="center"),
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
        dmc.Divider(
            label="At a Glance Stats", variant="dashed", labelPosition="center"
        ),
        dmc.Space(h="sm"),
        dmc.SimpleGrid(
            [
                html.Div(id="div-cards-total-ridership"),
                html.Div(id="div-cards-highest-recovery"),
            ],
            cols=2,
            spacing="md",
            verticalSpacing="xs",
        ),
        dmc.Space(h="sm"),
        dmc.Divider(variant="dashed"),
        dmc.Space(h="md"),
        modal_llm_setting,
        modal_llm_context,
        dmc.Center(llm_question),
        dmc.Space(h="sm"),
        dmc.Group(
            [
                dmc.ActionIcon(
                    DashIconify(icon="clarity:settings-line", width=20),
                    size="lg",
                    variant="gradient",
                    id="modal-llm-setting-button",
                ),
                dmc.ActionIcon(
                    DashIconify(icon="clarity:eye-show-line", width=20),
                    size="lg",
                    variant="gradient",
                    id="modal-llm-context-button",
                ),
                dmc.Button(
                    "Generate Insight", id="button-llm", variant="gradient", size="sm"
                ),
            ],
            justify="center",
            align="center",
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
