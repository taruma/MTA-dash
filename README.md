# MTA Ridership Explorer

An interactive dashboard to explore MTA (Metropolitan Transportation Authority) ridership trends and post-pandemic recovery patterns in New York City.

## Features

- Interactive visualization of ridership data across different MTA services:
  - 🚆 Subways
  - 🚌 Buses
  - 🚄 Long Island Rail Road (LIRR)
  - 🚉 Metro-North Railroad
  - 🚐 Access-A-Ride Paratransit
  - 🌉 Bridges and Tunnels
  - 🚋 Staten Island Railway

- Analyze data with flexible views:
  - Daily
  - Weekly 
  - Monthly
  - Yearly

- Compare both absolute ridership numbers and recovery percentages vs pre-pandemic levels
- Date range selection
- Multi-mode comparison
- AI-powered insights using LLM integration

## Installation

Requires Python 3.12+

```sh
# Run the dashboard
uv run app.py
```

## Tech Stack
- Dash
- Plotly
- Pandas
- OpenAI (for LLM insights)
- Dash Mantine Components
- Dash Bootstrap Components

## Data Source

Dataset sourced from [Plotly Datasets](https://github.com/plotly/datasets/tree/master/App-Challenges/MTA-NYC)\
