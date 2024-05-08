import yfinance as yf


def analyze_price_trend(symbol, period):
    """
  This function downloads historical price data for a stock and analyzes the trend for a given period.

  Args:
      symbol (str): The stock ticker symbol.
      period (str): The time period for analysis (e.g., "1y", "1m", "W-MON", "Q").

  Returns:
      str: A message describing the overall price trend for the given period.
  """

    # Download data for the specified period
    try:
        data = yf.download(symbol, period=period)
    except (ConnectionError, ValueError) as e:
        print(f"Error downloading data for {symbol}: {e}")
        return None

    # Check if data is empty
    if data.empty:
        print(f"No data found for {symbol}")
        return None

    # Calculate the closing price difference
    price_diff = data['Close'][-1] - data['Close'][0]

    # Analyze the trend based on price difference
    if price_diff > 0:
        trend = "upward"
    elif price_diff < 0:
        trend = "downward"
    else:
        trend = "sideways"

    return f"The overall price trend for {symbol} over the past {period} is {trend}."


if __name__ == "__main__":
    # Get user input for stock symbol and time period
    symbol = input("Enter a stock symbol (e.g., AAPL, TSLA): ")

    # Get valid time period input
    valid_periods = ["1y", "1m", "W-MON", "Q"]
    while True:
        period = input("Enter time period (yearly: 1y, monthly: 1m, weekly-starting-monday: W-MON, quarterly: Q): ")
        if period in valid_periods:
            break
        else:
            print(f"Invalid period. Valid options are: {', '.join(valid_periods)}")

    # Analyze and print the trend
    trend_message = analyze_price_trend(symbol, period)

    if trend_message:
        print(trend_message)
