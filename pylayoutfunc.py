"""Module for layout functions."""

import dash_mantine_components as dmc
import pyfunc

def generate_card_total_ridership(label, total_ridership):
    """Generate a card with total ridership."""

    card = dmc.Card(
        children=[
            dmc.CardSection(withBorder=True, bg="gray", h="0.5rem"),
            dmc.Text(
                "Total Ridership Reached", size="xs", fs="italic", ta="center", mt="xs"
            ),
            dmc.Text(
                dmc.NumberFormatter(value=total_ridership, thousandSeparator=True),
                size="xl",
                fw=700,
                ta="center",
            ),
            dmc.Text(f"for {label}", fw=300, lts="0.05rem", size="xs", ta="center"),
        ],
        withBorder=True,
        shadow="md",
        radius="md",
    )

    return card


def generate_card_highest_recovery(
    label, total_ridership, time_label, highest_date, percent_recovery
):
    card = dmc.Card(
        children=[
            dmc.CardSection(withBorder=True, bg="blue", h="0.5rem", mb="xs"),
            dmc.Text(
                f"{label} hit a high of",
                size="xs",
                ta="center",
                lts="0.05rem",
                fw=300,
                mb="xs",
            ),
            dmc.Group(
                [
                    dmc.Text(
                        dmc.NumberFormatter(
                            value=total_ridership, thousandSeparator=True
                        ),
                        size="sm",
                        fw=500,
                    ),
                    dmc.Text(f" {time_label.lower()} ridership on", size="sm"),
                ],
                justify="center",
                gap=5,
            ),
            dmc.Text(
                f"{highest_date}",
                size="xl",
                fw=700,
                ta="center",
            ),
            dmc.Group(
                [
                    dmc.Text("with a peak recovery of ", size="sm", fs="italic"),
                    dmc.Text(f"{percent_recovery:.2f}%", fw=700, size="sm", fs="italic"),
                ],
                justify="center",
                gap=5,
            ),
        ],
        withBorder=True,
        shadow="md",
        radius="md",
    )

    return card


# LAYOUT FUNCTIONS


def generate_layout_card_total_ridership(
    mta_data: dict,
    selected_modes: list = None,
    start_date: str = None,
    end_date: str = None,
) -> dmc.Group:
    """Generate a layout card with total ridership."""

    selected_cards = []

    for mode in selected_modes:
        filtered_ridership = mta_data[mode]["data_ridership"].loc[start_date:end_date]
        total_ridership = filtered_ridership.sum()

        card = generate_card_total_ridership(mta_data[mode]["label"], total_ridership)
        selected_cards.append(card)

    return dmc.Group(
        selected_cards,
        justify="center"
    )


def generate_layout_card_highest_recovery(
    mta_data: dict,
    selected_modes: list = None,
    start_date: str = None,
    end_date: str = None,
    time_frequency: str = None,
):
    
    selected_cards = []

    time_label = pyfunc.TIME_FREQUENCY_DICT[time_frequency]

    for mode in selected_modes:
        filtered_ridership = mta_data[mode]["data_ridership"].loc[start_date:end_date]
        filtered_recovery = mta_data[mode]["data_recovery"].loc[start_date:end_date]

        resample_ridership = filtered_ridership.resample(time_frequency).sum()
        resample_recovery = filtered_recovery.resample(time_frequency).mean()

        highest_recovery = resample_recovery.max()
        highest_date = resample_recovery.idxmax().strftime("%B %d, %Y")

        total_ridership = resample_ridership.loc[highest_date]

        card = generate_card_highest_recovery(
            mta_data[mode]["label"],
            total_ridership,
            time_label,
            highest_date,
            highest_recovery,
        )

        selected_cards.append(card)

    return dmc.Group(
        selected_cards,
        justify="center",
    )
