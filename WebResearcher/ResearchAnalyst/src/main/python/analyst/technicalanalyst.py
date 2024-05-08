import yfinance as yf
import pandas as pd
import ta


def calculate_technical_indicators(stock_symbol, start_date, end_date):
    # Download historical data
    data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Calculate technical indicators
    data['SMA_50'] = ta.trend.sma_indicator(data['Close'], window=50)
    data['SMA_200'] = ta.trend.sma_indicator(data['Close'], window=200)
    data['RSI'] = ta.momentum.rsi(data['Close'])

    # Extracting the last row (latest values)
    last_row = data.iloc[-1]

    # Extracting technical analysis parameters
    sma_50 = last_row['SMA_50']
    sma_200 = last_row['SMA_200']
    rsi = last_row['RSI']

    # Outputting the technical analysis parameters
    print(f"Technical Analysis for {stock_symbol} (Latest Data)")
    print(f"SMA 50: {sma_50}")
    print(f"SMA 200: {sma_200}")
    print(f"RSI: {rsi}")


# Example usage
if __name__ == "__main__":
    stock_symbol = "AAPL"  # Stock symbol (e.g., AAPL for Apple)
    start_date = "2021-01-01"  # Start date
    end_date = "2021-12-31"  # End date

    calculate_technical_indicators(stock_symbol, start_date, end_date)
