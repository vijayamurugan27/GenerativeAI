import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# # Fetch historical data for Tata Motors
# ticker = 'TATAMOTORS.NS'
# data = yf.download(ticker, start='2023-01-01', end='today')

# # Check the data
# print(f"Ticker: {ticker}")
# print(data.head())

# Get TATA Motors' historical data
tatamotors = yf.Ticker('TATAMOTORS.NS')

# Fetch current day's stock price
current_day_price = tatamotors.history(period='1d')['Close']

# Fetch last 30 days of historical data for plotting
last_month_data = tatamotors.history(period='1mo')

# Plot the close prices to show yearly change
plt.figure(figsize=(14, 7))
plt.title('Tata Motors Closing Prices (YTD)')
sns.lineplot(x=data.index, y=data['Close'], label=f"{ticker}")

# Customize plot
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()