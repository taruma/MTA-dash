# MTA Ridership Explorer: Trends and Post-Pandemic Recovery

![License](https://img.shields.io/badge/License-MIT-blue.svg)

This interactive dashboard, "MTA Ridership Explorer," provides a comprehensive view into ridership trends and post-pandemic recovery across the Metropolitan Transportation Authority (MTA) network in New York City. Explore daily ridership data across various MTA services, including subways, buses, commuter rails (LIRR and Metro-North), paratransit (Access-A-Ride), bridges and tunnels, and the Staten Island Railway. The dashboard aims to highlight ridership patterns since the start of the COVID-19 pandemic, offering a glimpse into recovery trends and the current state of public transit usage. Users can switch between daily, weekly, monthly, and yearly views to examine the data and compare both absolute ridership numbers and the percentage recovered compared to pre-pandemic levels.

## Features

- **📊 Interactive Trend Analysis:** Visualize ridership recovery trends with interactive line charts, comparing both estimated ridership volumes and percentage drops from pre-pandemic levels.
- **🚆🚌 Multi-Service Selection:**  Analyze any combination of MTA's services – Subways, Buses, Long Island Rail Road, Metro-North, Access-A-Ride, Bridges and Tunnels, and Staten Island Railway – to uncover distinct recovery patterns.
- **🗓️ Flexible Timeframes:**  Adjust the analysis period using start and end date selectors to focus on specific time windows and observe recovery rates over different durations.
- **📅 Granular Data Aggregation:** Switch between daily, weekly, monthly, and yearly views to gain insights into short-term fluctuations and long-term trends.
- **📈 At-a-Glance Statistics:** Quickly grasp key performance indicators such as peak ridership and recovery percentages for each selected service.
- **🤖 AI-Powered Insights:** Leverage the power of Large Language Models (LLMs) to generate insightful narratives and summaries of the displayed ridership trends, adding context and understanding to the visualizations. *(Note: Remember to independently verify LLM-generated insights.)*
- **💻 Open Source & Customizable:** The code for this dashboard is available on GitHub, allowing for customization and extension.


## Installation

Requires **Python 3.12**

1. **Clone the repository**:
    ```sh
    git clone https://github.com/taruma/mta-dash.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd mta-dash
    ```
3. **Configure Environment Variables**:
    - Create a `.env` file in the project root directory.
    - Add the required environment variables. For example:
        ```env
        OPENAI_API_KEY=your_openai_api_key
        ```
4. **Enable Debug Mode (Optional for Development)**:
    - Open `appconfig.py` in a text editor.
    - Uncomment the following lines to enable debug mode:
        ```python
        # appconfig.dash.debug = True
        ```
    - This will allow detailed error messages and enable live reload during development.
5. **Run & Install the dashboard**:
    ```sh
    uv run app.py
    ```
    
## Usage

After running the dashboard, open your browser and navigate to your app to start exploring MTA ridership data.

## Data Source

Dataset sourced from [Plotly Datasets](https://github.com/plotly/datasets/tree/master/App-Challenges/MTA-NYC).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Note

This app was created as a submission for the [Plotly & Maven Analytics Holiday Season App Challenge](https://community.plotly.com/t/holiday-season-app-challenge-nyc-mta/88389).