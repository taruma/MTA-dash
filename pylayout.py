"""Layout Module for Dash App"""

import dash_mantine_components as dmc
from dash import dcc, html
from appconfig import appconfig
import pyfigure

# APPCONFIG
main_title_text = appconfig.dash.title
main_subtitle_text = appconfig.dash.subtitle

# MAIN ========================================

# TITLE
main_title = dmc.Title(main_title_text, order=1)
main_subtitle = dmc.Text(main_subtitle_text, c="dimmed", style={"fontSize": "1.2rem"})

# PLOT-1
plot_title = dmc.Title("Plot 1", order=2, my="md")
plot_1 = dcc.Graph(
    id="plot-1",
    figure=pyfigure.generate_empty_figure("hello")
)






# APPSHELL ====================================

appshell_main = dmc.AppShellMain(
    [
        main_title,
        main_subtitle,
        dmc.Divider(variant="solid"),
        plot_title,
        plot_1
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
