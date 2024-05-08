import yfinance as yf


def fundamental_analysis(symbol):
    """
  Performs basic fundamental analysis for a given stock symbol.

  Args:
      symbol: The stock ticker symbol.

  Returns:
      A dictionary containing key financial metrics or None if data fails to load.
  """
    # Download financial data using yfinance
    try:
        data = yf.download(symbol, period="1y", auto_adjust=True)
        print(data)
    except (ConnectionError, ValueError):
        return None

    # Check if data is downloaded successfully
    if data.empty:
        return None

    # Calculate basic financial metrics
    metrics = {}
    if "EPS" in data.columns:
      metrics["EPS"] = data["EPS"].mean()  # Average EPS over the past year
    else:
      metrics["EPS"] = None  # Set EPS to None if not available
    metrics["EPS"] = data["EPS"].mean()  # Average EPS over the past year
    metrics["P_E"] = data["Close"].iloc[-1] / metrics["EPS"]  # Current P/E ratio
    metrics["Revenue_Growth"] = (data["Revenue"].iloc[-1] - data["Revenue"].iloc[0]) / data["Revenue"].iloc[
        0] * 100  # YoY revenue growth
    metrics["Profit_Margin"] = (data["EBIT"] / data["Revenue"]).mean() * 100  # Average profit margin
    metrics["Debt_to_Equity"] = data["Total Long Term Debt"].iloc[-1] / data["Total Stockholders' Equity"].iloc[-1]
    metrics["Free_Cash_Flow"] = data["Free Cash Flow"].iloc[-1]
    metrics["ROE"] = data["Net Income"] / data["Total Stockholders' Equity"].iloc[-1] * 100  # ROE for the latest year
    metrics["Dividend_Yield"] = data["Trailing Annual Dividend Yield"] * 100  # Annualized dividend yield

    return metrics


if __name__ == "__main__":

    symbol = input("Enter stock symbol: ")
    metrics = fundamental_analysis(symbol)

    if metrics:
        print("Financial Metrics for", symbol)
        for metric, value in metrics.items():
            print(f"{metric}: {value:.2f}")
    else:
        print("Failed to retrieve data for", symbol)
