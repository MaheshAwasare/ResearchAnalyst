import yfinance as yf


def calculate_support_resistance(symbol, period):
    """
  This function downloads historical price data and calculates potential support and resistance zones.

  Args:
      symbol (str): The stock ticker symbol.
      period (str): The time period for data (refer to yfinance documentation).

  Returns:
      dict: A dictionary containing  support and resistance levels.
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

    # Calculate potential support and resistance
    support = data['Low'].min()
    resistance = data['High'].max()

    return {
        "Symbol": symbol,
        "Period": period,
        "Potential Support": support,
        "Potential Resistance": resistance
    }


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

    # Calculate and print results
    results = calculate_support_resistance(symbol, period)

    if results:
        print(f"**Results for {symbol} ({period})**")
        print(f"Potential Support: {results['Potential Support']}")
        print(f"Potential Resistance: {results['Potential Resistance']}")
        print(
            "**Disclaimer:** These are calculated values and may not be exact support and resistance levels. Further "
            "analysis is recommended.")
    else:
        print("Failed to calculate support and resistance levels.")
