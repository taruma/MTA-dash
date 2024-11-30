"""This module contains functions for processing data and generating reports."""

import base64
import pandas as pd

PATH_DATASET = "data/MTA_Daily_Ridership.csv"
MTA_COLUMN_NAMES = [
    "date",
    "subway_ridership",
    "subway_recovery",
    "bus_ridership",
    "bus_recovery",
    "lirr_ridership",
    "lirr_recovery",
    "mnr_ridership",
    "mnr_recovery",
    "aar_trips",
    "aar_recovery",
    "bt_traffic",
    "bt_recovery",
    "sir_ridership",
    "sir_recovery",
]
RIDERSHIP_SUFFIXES = ["ridership", "trips", "traffic"]
TRANSPORTATION_MODES = ["subway", "bus", "lirr", "mnr", "aar", "bt", "sir"]
TRANSPORTATION_NAMES = [
    "Subways",
    "Buses",
    "Long Island Rail Road",
    "Metro North",
    "Access-A-Ride",
    "Bridges and Tunnels",
    "Staten Island Railway",
]
TRANSPORTATION_EMOJI = ["🚆", "🚌", "🚄", "🚉", "🚐", "🌉", "🚋"]

ridership_columns = [
    column
    for column in MTA_COLUMN_NAMES
    if any(suffix in column for suffix in RIDERSHIP_SUFFIXES)
]
recovery_columns = [col for col in MTA_COLUMN_NAMES if "recovery" in col]


def get_mta_daily(path_dataset: str = PATH_DATASET) -> pd.DataFrame:
    """Get MTA daily data."""
    mta_daily_ridership = pd.read_csv(path_dataset)
    mta_daily_ridership.columns = MTA_COLUMN_NAMES
    mta_daily = mta_daily_ridership.assign(
        date=pd.to_datetime(mta_daily_ridership["date"])
    ).set_index("date")

    return mta_daily


def get_mta_ridership_recovery(
    mta_daily: pd.DataFrame, is_ridership: bool = True
) -> pd.DataFrame:
    """Get MTA ridership or recovery data."""
    if is_ridership:
        return mta_daily[ridership_columns]
    else:
        return mta_daily[recovery_columns]

def read_text_file(file_path):
    """Read text file and return content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None
    
def fig_to_base64(fig):
    # Convert plot to PNG image
    img_bytes = fig.to_image(format="png")
    fig.write_image("fig.png")
    
    # Encode to base64
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    
    # Create base64 string format commonly used in APIs
    img_base64_str = f"data:image/png;base64,{img_base64}"
    
    return img_base64_str