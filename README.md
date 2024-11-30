# MTA Ridership Explorer

![License](https://img.shields.io/badge/License-MIT-blue.svg)

An interactive dashboard to explore MTA (Metropolitan Transportation Authority) ridership trends and post-pandemic recovery patterns in New York City.

## Features

- **Interactive Visualization** of ridership data across different MTA services:
  - 🚆 **Subways**
  - 🚌 **Buses**
  - 🚄 **Long Island Rail Road (LIRR)**
  - 🚉 **Metro-North Railroad**
  - 🚐 **Access-A-Ride Paratransit**
  - 🌉 **Bridges and Tunnels**
  - 🚋 **Staten Island Railway**

- **Flexible Data Views**:
  - Daily
  - Weekly 
  - Monthly
  - Yearly

- **Comparative Analysis**:
  - Absolute ridership numbers
  - Recovery percentages vs pre-pandemic levels

- **Date Range Selection**  
- **Multi-mode Comparison**
- **AI-powered Insights** using LLM integration

## Installation

Requires **Python 3.12**

1. Clone the repository:
    ```sh
    git clone https://github.com/taruma/mta-dash.git
    ```
2. Navigate to the project directory:
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
5. Run & Install the dashboard:
    ```sh
    uv run app.py
    ```
## Usage

After running the dashboard, open your browser and navigate to your app to start exploring MTA ridership data.

## Data Source

Dataset sourced from [Plotly Datasets](https://github.com/plotly/datasets/tree/master/App-Challenges/MTA-NYC)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Note

This app was created as a submission for the [Plotly & Maven Analytics Holiday Season App Challenge](https://community.plotly.com/t/holiday-season-app-challenge-nyc-mta/88389).