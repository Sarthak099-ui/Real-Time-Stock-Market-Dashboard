import streamlit as st
import data_fetcher as df
import visualizer as viz

# 1. Page Configuration
st.set_page_config(page_title="Stock Dashboard", page_icon="📈", layout="wide")

# 2. Sidebar for User Inputs
st.sidebar.header("Dashboard Controls")
ticker_input = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, INFY.NS):", "AAPL").upper()
time_period = st.sidebar.selectbox("Select Time Period:", ["1mo", "3mo", "6mo", "1y", "2y", "5y"])

# 3. Main Dashboard Header
st.title("📈 Real-Time Stock Market Dashboard")
st.markdown("Built by a 1st Year B.Tech CSE (AI & ML) Student")

# 4. Fetching Data using our Data Engine
with st.spinner(f"Fetching data for {ticker_input}..."):
    stock_info = df.get_stock_info(ticker_input)
    historical_data = df.get_historical_data(ticker_input, period=time_period)

# 5. Displaying the Dashboard Content
if stock_info and historical_data is not None:
    
    # --- Top Section: Key Metrics ---
    st.subheader(f"**{stock_info['name']} ({ticker_input})**")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Price", f"{stock_info['current_price']} {stock_info['currency']}")
    with col2:
        st.metric("Day High", f"{stock_info['high']} {stock_info['currency']}")
    with col3:
        st.metric("Day Low", f"{stock_info['low']} {stock_info['currency']}")

    st.divider()

    # --- Middle Section: The Interactive Chart ---
    st.subheader("Technical Chart (Price & Moving Averages)")
    
    # This safely calls the visualizer engine we built earlier!
    fig = viz.create_candlestick_chart(historical_data, stock_info['name'])
    if fig:
        st.plotly_chart(fig, use_container_width=True)
        
    # --- Bottom Section: Raw Data ---
    with st.expander("View Raw Historical Data"):
        st.dataframe(historical_data.tail())

else:
    st.error("Oops! Could not fetch data. Please check the stock ticker symbol and try again.")