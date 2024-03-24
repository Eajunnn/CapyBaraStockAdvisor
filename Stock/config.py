import requests
from dataclasses import dataclass

@dataclass
class Config:
    ollamaHost: str = "172.22.45.57"  # Use 172.22.45.57 for llama within WSL FIXME: VPN
    ollamaPort: str = "11434"
    ollamaModelName: str = 'llama2:13b'
    ollamaModelContextSize: int =  512
    databseURL: str = 'mongodb://localhost:27017'
    
    @property
    def ollamaUrl(self) -> str:
        return f"http://{self.ollamaHost}:{self.ollamaPort}"