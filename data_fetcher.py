import yfinance as yf
import pandas as pd

def get_stock_info(ticker_symbol):
    """
    Fetches key real-time information for a given stock ticker.
    """
    try:
        # Connect to the specific stock ticker (e.g., 'AAPL' or 'GOOGL')
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        
        # Extract only the key details we need for our dashboard
        stock_data = {
            "name": info.get("longName", "N/A"),
            "current_price": info.get("currentPrice", info.get("regularMarketPrice", 0.0)),
            "open": info.get("regularMarketOpen", 0.0),
            "high": info.get("regularMarketDayHigh", 0.0),
            "low": info.get("regularMarketDayLow", 0.0),
            "volume": info.get("regularMarketVolume", 0),
            "currency": info.get("currency", "USD")
        }
        return stock_data
    except Exception as e:
        print(f"Error fetching live info for {ticker_symbol}: {e}")
        return None

def get_historical_data(ticker_symbol, period="1mo", interval="1d"):
    """
    Fetches historical stock data and calculates Technical Indicators (Moving Averages).
    Period options: '1d', '5d', '1mo', '6mo', '1y', 'max'
    Interval options: '1m', '5m', '1d', '1wk'
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        # Download historical data as a Pandas DataFrame
        df = ticker.history(period=period, interval=interval)
        
        if df.empty:
            return None
        
        # Reset index so the 'Date' becomes a normal column we can work with easily
        df = df.reset_index()
        
        # --- DATA ANALYSIS / DATA CLEANING ---
        # Calculate 20-day Simple Moving Average (SMA)
        # 'Close' is the closing price of the stock. .rolling(window=20) looks at 20 rows at a time.
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        
        # Calculate 50-day Simple Moving Average (SMA)
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        
        return df
    except Exception as e:
        print(f"Error fetching historical data for {ticker_symbol}: {e}")
        return None