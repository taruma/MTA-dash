"""Layout Module for Dash App"""

import dash_mantine_components as dmc
from dash import dcc
from appconfig import appconfig
import pyfigure
from datetime import date
import pyfunc
from dash_iconify import DashIconify

# APPCONFIG
main_title_text = appconfig.dash.title
main_subtitle_text = appconfig.dash.subtitle

# MAIN ========================================

# TITLE
main_title = dmc.Center(dmc.Title(main_title_text, order=1, mt="xl"))
main_subtitle = dmc.Center(
    dmc.Text(main_subtitle_text, c="dimmed", style={"fontSize": "1.2rem"})
)

# SHORT DESCRIPTION

DESRIPTION = pyfunc.read_text_file("text/app_description.md")

short_description = dmc.Center(
    dmc.Paper(
        dcc.Markdown(DESRIPTION),
        shadow="lg",
        mt="md",
        w="80%",
        pt="md",
        px="lg",
    )
)

# PLOT-1
plot_title = dmc.Title("MTA Ridership Trends", order=2, my="md")
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


# APPSHELL ====================================

appshell_main = dmc.AppShellMain(
    [
        main_title,
        main_subtitle,
        dmc.Divider(variant="solid"),
        dmc.Center(short_description),
        dmc.Center(plot_title),
        plot_description,
        dmc.Group(
            [multi_select, date_picker_start, date_picker_end, resample_period_radio],
            justify="center",
            align="top",
        ),
        plot_mta_ridership_trends,
        dmc.Space(h="xl"),
        dmc.Divider(variant="solid"),
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
