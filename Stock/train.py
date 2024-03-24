import ollama

modelfile='''
FROM llama2:13b
SYSTEM You are CapybaraAI.
'''
try:
    # Create the model using ollama.create
    ollama.create(model='CapybaraAI', modelfile=modelfile)
    print("Model 'CapybaraAI' created successfully!")
except Exception as e: 
    print(f"Error creating model: {e}")