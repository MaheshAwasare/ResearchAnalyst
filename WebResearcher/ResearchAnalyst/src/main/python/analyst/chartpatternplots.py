import yfinance as yf
import matplotlib.pyplot as plt


def download_price_data(symbol, period):
    """
  Downloads historical closing price data for the given stock and period.

  Args:
      symbol (str): The stock ticker symbol.
      period (str): The time period for data (refer to yfinance documentation).

  Returns:
      pandas.DataFrame: A DataFrame containing the date and closing price.
  """

    try:
        data = yf.download(symbol, period=period)["Close"]
    except (ConnectionError, ValueError) as e:
        print(f"Error downloading data for {symbol}: {e}")
        return None

    return data.to_frame(name="Price")


def visualize_price_chart(data, symbol):
    """
  Creates a price chart for the given data and symbol.

  Args:
      data (pandas.DataFrame): A DataFrame containing date and closing price.
      symbol (str): The stock ticker symbol.
  """

    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Price"], marker="o")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title(f"Price Chart for {symbol}")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Get user input for stock symbol and time period
    symbol = input("Enter a stock symbol (e.g., AAPL, TSLA): ")
    valid_periods = ["1y", "1m", "W-MON", "Q"]
    while True:
        period = input("Enter time period (refer to yfinance documentation): ")
        if period in valid_periods:
            break
        else:
            print(f"Invalid period. Valid options are: {', '.join(valid_periods)}")

    # Download data
    data = download_price_data(symbol, period)

    # Check for successful download
    if data is not None:
        visualize_price_chart(data, symbol)
        print(
            "**Please note:** This program cannot automatically identify chart patterns. Visual inspection of the chart is recommended.")
    else:
        print("Failed to download data. Please try again.")
