import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import logging
from config import Config
import llama
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Global variables
chat_history = []
i = 0

# TODO: Display multiple stock market simulations concurrently (two lines in a graph)
#TODO: Refactor lines
#TODO: Try to combine LLM with graph
def plot_stock_price(stock_symbol1, stock_symbol2):
    times = []
    prices1 = []
    prices2 = []

    # Initial plot
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    line1, = ax.plot(times, prices1, label= stock_symbol1)
    line2, = ax.plot(times, prices2, label= stock_symbol2)
    ax.legend()  # Show legend for line labels
    
    plt.show()  # Display the initial plot

    while True:
        # Extracting the market prices
        share_info1 = yf.Ticker(stock_symbol1).info
        share_info2 = yf.Ticker(stock_symbol2).info
        
        # Try accessing different keys for market price
        market_price_keys = ['regularMarketPrice', 'currentPrice', 'lastPrice']
        market_price1 = None
        market_price2 = None
        for key in market_price_keys:
            if key in share_info1:
                market_price1 = share_info1[key]
            if key in share_info2:
                market_price2 = share_info2[key]
            if market_price1 and market_price2:
                break

        if market_price1 is None or market_price2 is None:
            print("Market price not found in available keys.")
            break

        current_time = datetime.datetime.now()
        times.append(current_time)
        prices1.append(market_price1)
        prices2.append(market_price2)

        # Limit the number of data points to display (change if you want to)
        max_display_points = 500
        if len(times) > max_display_points:
            times = times[-max_display_points:]
            prices1 = prices1[-max_display_points:]
            prices2 = prices2[-max_display_points:]

        # Update the plot
        line1.set_xdata(times)
        line1.set_ydata(prices1)
        line2.set_xdata(times)
        line2.set_ydata(prices2)

        buffer_zone = 100  # Adjust buffer zone as needed (The space above and below line)
        min_price = min(min(prices1), min(prices2)) - buffer_zone
        max_price = max(max(prices1), max(prices2)) + buffer_zone
        ax.set_ylim(min_price, max_price)

        ax.relim()
        ax.autoscale_view()

        plt.draw()
        plt.pause(1)  # Update every 1 second (change if you want to)

if __name__ == "__main__":
    stock_symbol1 = input("Enter stock symbol for Simulation 1: ")
    stock_symbol2 = input("Enter stock symbol for Simulation 2: ")
    plot_stock_price(stock_symbol1, stock_symbol2)
