"""Module for layout functions."""

import dash_mantine_components as dmc
import pyfunc
import pandas as pd


def generate_card_total_ridership(label, total_ridership):
    """Generate a card with total ridership."""

    card = dmc.Card(
        children=[
            dmc.Text("Total Ridership Reached", size="xs", fs="italic", ta="center"),
            dmc.Text(
                dmc.NumberFormatter(value=total_ridership, thousandSeparator=True),
                size="xl",
                fw=700,
                ta="center",
            ),
            dmc.Text(
                f"for {label}",
                fw=300,
                lts="0.05rem",
                size="xs",
                ta="center",
            ),
        ],
        withBorder=True,
        shadow="md",
        radius="md",
        # w=250,
    )

    return card


def generate_layout_card_total_ridership(
    mta_daily_ridership: pd.DataFrame,
    resample_period: str = None,
    date_start: str = None,
    date_end: str = None,
    modes: list = None,
):
    """Generate a layout card with total ridership."""

    # TODO: Refactor this with pyfigure.generate_ridership_recovery

    resample_period = "W" if resample_period is None else resample_period
    date_start = mta_daily_ridership.index.min() if date_start is None else date_start
    date_end = mta_daily_ridership.index.max() if date_end is None else date_end
    modes = pyfunc.TRANSPORTATION_MODES if (modes is None) or (not modes) else modes

    mta_daily_ridership = mta_daily_ridership.loc[date_start:date_end]

    transportation_label = list(
        zip(
            pyfunc.TRANSPORTATION_MODES,
            pyfunc.TRANSPORTATION_NAMES,
            pyfunc.TRANSPORTATION_EMOJI,
        )
    )

    selected_transportation_label = [
        (mode, name, emoji)
        for mode, name, emoji in transportation_label
        if mode in modes
    ]

    selected_cards = []
    for mode, name, emoji in selected_transportation_label:
        ridership_column = [
            col for col in mta_daily_ridership.columns if col.startswith(mode)
        ][0]

        total_ridership = mta_daily_ridership[ridership_column].sum()
        label = f"{emoji} {name}"
        selected_cards.append(generate_card_total_ridership(label, total_ridership))

    return dmc.Group(
        selected_cards,
        justify="center",
        mt="md",
    )
