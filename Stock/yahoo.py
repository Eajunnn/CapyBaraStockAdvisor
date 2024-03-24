import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import datetime
import logging
from config import Config
import llama

# Global variables
chat_history = []

# TODO: Implement user interface for managing multiple stock market simulations concurrently(two lines in a graph)
def plot_stock_price(stock_symbol):
    times = []
    prices = []

    # Initial plot
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    line, = ax.plot(times, prices)

    # CHATBOX
    text_box_ax = plt.axes([0.1, 0.01, 0.8, 0.05])
    text_box = TextBox(text_box_ax, 'ChatBox')


    
    #TODO: Modifying the system_meassage
    
    def chat(text):
        nonlocal stock_symbol
        message = text
        print("Question: " + message)
        text_box.set_val("")
        systemMessage = """
            You are a cute capybara
        """.strip().replace("\n", " ")

        logging.info("System message: %s", systemMessage)
        print("CapyBara generating...")

        # Llama generate response here
        try:
            response = llama.chat(model= Config.ollamaModelName, messages=[
                {
                    'role': 'system',
                    'content': systemMessage,
                },
                {
                    'role': 'system',
                    'content': message,  
                },
                ])
            response_message = response['message']['content']
            chat_history.append(response_message)  # Store the response in chat history
            print("Capybara:" + response_message)

            # Print only the second answer in the terminal
            if len(chat_history) >= 2:
                print("Second Answer:", chat_history[1])  # Print the second answer

        # Clear the chat history after printing the second answer
            chat_history.clear()
        except Exception:
            logging.error("Failed to generate response for message: %s", message, exc_info=True)
    
    text_box.on_submit(chat)
    
    while True:
        # Extracting the market price
        share_info = yf.Ticker(stock_symbol).info

        # Try accessing different keys for market price
        market_price_keys = ['regularMarketPrice', 'currentPrice', 'lastPrice']
        market_price = None
        for key in market_price_keys:
            if key in share_info:
                market_price = share_info[key]
                break

        if market_price is None:
            print("Market price not found in available keys.")
            break

        current_time = datetime.datetime.now()
        times.append(current_time)
        prices.append(market_price)

        # Limit the number of data points to display(change if you want to)
        max_display_points = 50
        if len(times) > max_display_points:
            times = times[-max_display_points:]
            prices = prices[-max_display_points:]

        # Update the plot
        line.set_xdata(times)
        line.set_ydata(prices)
        
        # Set y-axis limits based on min and max prices in the data
        min_price = min(prices)
        max_price = max(prices)
        padding = 1 
        ax.set_ylim(min_price - padding, max_price + padding)

        ax.relim()
        ax.autoscale_view()
        
        plt.draw()
        plt.pause(1)  # Update every 1 second(change if you want to)

if __name__ == "__main__":
    stock_symbol = input("Enter stock symbol: ")
    plot_stock_price(stock_symbol)