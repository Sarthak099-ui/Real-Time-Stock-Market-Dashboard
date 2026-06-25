# MarketLens: Real-Time Stock Dashboard

An industrial-grade, interactive financial data dashboard built using Python, Streamlit, and Plotly. This application fetches live market statistics, tracks price movements via candlestick charts, and computes technical analysis indicators (Simple Moving Averages) in real-time.

Built as a foundational project for Data Engineering and Full-Stack Python development.

## Features

- Live Data Ingestion: Fetches real-time price, volume, high, and low metrics using the `yfinance` API.
- Advanced Visualizations: Renders multi-layered, interactive Plotly Candlestick charts optimized with a dark-mode user experience.
- Technical Indicators:Dynamically calculates 20-day and 50-day Simple Moving Averages (SMA) using Pandas for trend analysis.
- Responsive Controls: Fully customizable sidebar inputs to filter assets by ticker symbol (e.g., AAPL, TSLA, INFY.NS) and adjust historical timeframes.

##  Tech Stack & Architecture

- Frontend:Streamlit (Web UI Framework)
- Data Visualization:Plotly Graph Objects (Interactive Graphics Engine)
- Data Processing & Analytics: Python, Pandas
- Data Source: Yahoo Finance API (`yfinance`)

