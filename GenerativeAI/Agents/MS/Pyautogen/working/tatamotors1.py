import yfinance as yf
import matplotlib.pyplot as plt

def main():
    # Get TATA Motors' historical data
    tatamotors = yf.Ticker('TATAMOTORS.NS')

    # Fetch current day's stock price
    current_day_price = tatamotors.history(period='1d')['Close']

    # Fetch last 30 days of historical data for plotting
    last_month_data = tatamotors.history(period='1mo')

    print("Current Day Stock Price (as of today): £%.2f" % current_day_price.iloc[-1])

    # Plotting historical data
    plt.figure(figsize=(10, 5))
    plt.plot(last_month_data.index, last_month_data['Close'], label='TATA Motors Close Prices')
    plt.title('Tata Motors Stock Price Over Last Month')
    plt.xlabel('Date')
    plt.ylabel('Price (in ₹)')
    plt.legend()
    plt.grid(True)

    # Save the plot as a file
    plt.savefig('tatamotors_price_plot1.png')

if __name__ == "__main__":
    main()