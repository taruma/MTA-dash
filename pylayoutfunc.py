"""Module for layout functions."""

import dash_mantine_components as dmc


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
        justify="center",
        mt="md",
    )
