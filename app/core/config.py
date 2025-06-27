from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import Optional, Dict

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    # Embedding Model
    embedding_model: str = "text-embedding-3-small"
    
    # ChromaDB Settings
    chroma_persist_directory: Path = Path("./data/vectorstore")
    
    # Document Settings
    chunk_size: int = 1000
    chunk_overlap: int = 200
    
    # LLM Settings
    openai_api_key: str | None = None
    model_name: str = "gpt-3.5-turbo"
    
    # Web Loading Settings
    web_timeout: int = 30
    web_user_agent: str = "Simple-RAG/1.0"
    web_requests_per_second: int = 2
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create global settings instance
settings = Settings()

# Ensure directories exist
settings.chroma_persist_directory.parent.mkdir(parents=True, exist_ok=True) 