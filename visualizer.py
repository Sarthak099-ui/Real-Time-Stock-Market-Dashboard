import plotly.graph_objects as go

def create_candlestick_chart(df, stock_name):
    """
    Creates an interactive candlestick chart with moving averages.
    """
    # Safety check: If there is no data, return nothing
    if df is None or df.empty:
        return None

    # Create a blank canvas
    fig = go.Figure()

    # --- 1. The Candlestick Chart ---
    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Market Price'
    ))

    # --- 2. Add the 20-Day Moving Average Line ---
    if 'SMA_20' in df.columns:
        fig.add_trace(go.Scatter(
            x=df['Date'], y=df['SMA_20'], mode='lines', name='20-Day SMA', line=dict(color='cyan', width=1.5)
        ))

    # --- 3. Add the 50-Day Moving Average Line ---
    if 'SMA_50' in df.columns:
        fig.add_trace(go.Scatter(
            x=df['Date'], y=df['SMA_50'], mode='lines', name='50-Day SMA', line=dict(color='orange', width=1.5)
        ))

    # --- 4. Professional Dashboard Styling ---
    fig.update_layout(
        title=f"{stock_name} Stock Price History",
        yaxis_title="Stock Price",
        xaxis_title="Date",
        template="plotly_dark",
        xaxis_rangeslider_visible=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig