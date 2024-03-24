import socket

ollama_host = "172.22.45.57"  # Update with the IP address of WSL environment
ollama_port = 11434  # Update with the correct port for Ollama on Linux

try:
    # Check the connection with OLLama on Linux
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ollama_host, ollama_port))
        print("Connection to Ollama service successful.")
except Exception as e:
    print("Error connecting to Ollama service:", e)
