import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Get TATA Motors' historical data
ticker = 'TATAMOTORS.NS'
tatamotors = yf.Ticker(ticker)

# Fetch current day's stock price
current_day_price = tatamotors.history(period='1d')['Close']

# Fetch last 30 days of historical data for plotting
last_month_data = tatamotors.history(period='1mo')

# Plot the close prices to show yearly change
plt.figure(figsize=(14, 7))
plt.title('Tata Motors Closing Prices (YTD)')
sns.lineplot(x=last_month_data.index, y=last_month_data['Close'], label=f"{ticker}")

# Customize plot
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()