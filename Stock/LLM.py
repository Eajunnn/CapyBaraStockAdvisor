import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import logging
from config import Config
import llama
import torch

# Set CUDA device if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#TODO: The latency is too HIGH(Change to GPU)
#FIXME: The words are not coming out when generating
def LLM():
    # Set the CUDA device for PyTorch
    if torch.cuda.is_available():
        torch.cuda.set_device(0)  # Use GPU device 0

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
            Provide short answers but enough information
        """.strip().replace("\n", " ")

        logging.info("System message: %s", systemMessage)
        print("CapyBaraAI is generating response...")

        # Llama generate response here using the loaded model
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
