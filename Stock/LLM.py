import logging
from config import Config
import llama
import torch
from llama import Client
from pymongo import MongoClient

# Set CUDA device if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

connection_string = "mongodb+srv://eajun:eajun030802@cluster0.ktfe47o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize the MongoClient with your connection string
client = MongoClient(connection_string)

#FIXME: Cannot get the text for ..% keywords
db = client.Eajun
collection = db["textData"]

# Create a text index on the "keywords" field
collection.create_index([("keywords", "text")])

#TODO: The latency is too HIGH(Change to GPU)
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
            You should provide your own predictions on the future stock market if the question related to stock.
            You should provide more information on the stock market if the question related to stock.
            Provide short answers but enough information.
        """.strip().replace("\n", " ")

        logging.info("System message: %s", systemMessage)
        print("CapyBaraAI is generating response...")

        # Llama generate response here using the loaded model
        try:
            # client = Client(host='http://172.22.45.57:11434')
            stream = llama.chat(
                model='llama2:13b',
                messages=[
                    {
                        'role': 'system',
                        'content': systemMessage,
                    },
                    {
                        'role': 'system',
                        'content': message,
                    },
                ],
                stream=True,
            )
            # response_message = response['message']['content']
            print("CapybaraAI: ")
            for chunk in stream:    
                print(chunk['message']['content'], end='', flush=True)
            print("\n")

        except Exception:
            logging.error("Failed to generate response for message: %s", message, exc_info=True)

if __name__ == "__main__":
    LLM()
