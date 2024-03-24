import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import logging
from config import Config
import llama
import torch

#TODO: The latency is too HIGH
#FIXME: The words are not coming out when generating
def LLM():
    while True:
        message = input("Enter your question or type 'exit' to quit: ")
        if message.lower() == 'exit':
            break
        print("Question: " + message)
        systemMessage = """
            Your name is CapybaraAI. 
            Always introduce yourself first. 
            Behave yourself like a capybara but still answer like a Llama.
            You are a stock advisor for United State stock market.
            You should provide your own predictions on the future stock market.
            You should provide more information on the stock market.
        """.strip().replace("\n", " ")

        logging.info("System message: %s", systemMessage)
        print("CapyBaraAI is generating response...")

        # Llama generate response here
        try:
            response = llama.chat(model=Config.ollamaModelName, messages=[
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
            print("Capybara:" + response_message)

        except Exception:
            logging.error("Failed to generate response for message: %s", message, exc_info=True)
            
if __name__ == "__main__":
    LLM()