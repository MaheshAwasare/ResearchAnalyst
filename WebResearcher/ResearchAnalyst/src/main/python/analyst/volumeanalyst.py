import yfinance as yf


def analyze_volume_and_trend(symbol, period):
    """
  This function downloads historical data, calculates average daily volume, and interprets volume in the context of recent price trends.

  Args:
      symbol (str): The stock ticker symbol.
      period (str): The time period for data (refer to yfinance documentation).

  Returns:
      str: A message summarizing the average daily volume and potential implications.
  """

    try:
        data = yf.download(symbol, period=period)
    except (ConnectionError, ValueError) as e:
        print(f"Error downloading data for {symbol}: {e}")
        return None

    # Check if data is empty
    if data.empty:
        print(f"No data found for {symbol}")
        return None

    # Calculate average daily volume
    average_volume = data['Volume'].mean()

    # Analyze recent price change and volume
    recent_price_change = data['Close'][-1] - data['Close'][-2]
    recent_volume = data['Volume'][-1]

    # Interpret volume based on price movement
    if recent_price_change > 0 and recent_volume > average_volume:
        interpretation = "This could be a sign of a hot stock, with strong buying pressure indicated by the above average volume accompanying the price increase."
    elif recent_price_change < 0 and recent_volume > average_volume:
        interpretation = "High volume on a down day suggests strong selling pressure. This might not be a hot stock right now."
    else:
        interpretation = f"Average daily volume for the period is {average_volume:.2f}. Without a significant price change in either direction, it's difficult to say if this indicates a hot stock."

    return f"**Analysis for {symbol} ({period})**\nAverage Daily Volume: {average_volume:.2f}\n{interpretation}"


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

    # Analyze and print results
    analysis_message = analyze_volume_and_trend(symbol, period)

    if analysis_message:
        print(analysis_message)
    else:
        print("Failed to analyze volume and trend.")
