import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Global variables
chat_history = []
i = 0
plt.style.use('seaborn-darkgrid')



#TODO: Refactor lines so it can show multiple lines(Not only 2 lines)
#TODO: Try to combine LLM with graph
def plot_stock_price(stock_symbol):
    # Initial plot
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    ax.set_title("Stock Price Over Time ")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    lines = []
    
    for symbol in stock_symbol:
        times = []
        # prices1 = []
        # prices2 = []
        prices = []
    
        line, = ax.plot(times, prices, label= symbol)
        lines.append(line)
        # line2, = ax.plot(times, prices2, label= stock_symbol2)
        ax.legend()  # Show legend for line labels
    
        plt.show()  # Display the initial plot

    while True:
        for i,symbol in enumerate(stock_symbols):
            # Extracting the market prices
            share_info = yf.Ticker(symbol).info
            # share_info2 = yf.Ticker(stock_symbol).info
            # Try accessing different keys for market price
            market_price_keys = ['regularMarketPrice', 'currentPrice', 'lastPrice']
            market_price = None
            # market_price2 = None
            for key in market_price_keys:
                if key in share_info:
                    market_price = share_info[key]
                # if key in share_info2:
                #     market_price2 = share_info2[key]
            if market_price:
                #  if market_price is None:
                current_time = datetime.datetime.now()
                times.append(current_time)
                prices.append(market_price)
                # prices2.append(market_price2)
                # Limit the number of data points to display (change if you want to)
                max_display_points = 500
                if len(times) > max_display_points:
                    times = times[-max_display_points:]
                    prices = prices[-max_display_points:]
                    # prices2 = prices2[-max_display_points:]
                # Update the plot
                lines[i].set_xdata(times)
                lines[i].set_ydata(prices)
                # line2.set_xdata(times)
                # line2.set_ydata(prices2)
                
                
                buffer_zone = 100  # Adjust buffer zone as needed (The space above and below line)
                min_price = min(prices) - buffer_zone
                max_price = max(prices) + buffer_zone
                ax.set_ylim(min_price, max_price)
                ax.relim()
                ax.autoscale_view()
                plt.draw()
                plt.pause(1)  # Update every 1 second (change if you want to)

if __name__ == "__main__":
    n:int = int(input("Number of simulations to run: "))
    stock_symbols = []
    for i in range(n):
        symbols = input("Enter stock symbol for Simulation: ")
        stock_symbols.append(symbols) 
        # stock_symbol2 = input("Enter stock symbol for Simulation 2: ")
    plot_stock_price(stock_symbols)
