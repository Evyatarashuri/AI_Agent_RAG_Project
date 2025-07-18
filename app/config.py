# app/config.py
import os

class Config:
    # Flask App Configuration
    FLASK_APP = os.getenv("FLASK_APP", "app.main")
    FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST", "0.0.0.0")

    # MongoDB Configuration
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")

    # ChromaDB Configuration
    CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "papers")

    # Ollama Models Configuration
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
    CHAT_MODEL = os.getenv("CHAT_MODEL", "mistral-custom")
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")

    # Embedding Chunk Size
    MAX_CHUNK_SIZE = int(os.getenv("MAX_CHUNK_SIZE", "500"))

    # Swagger UI Configuration
    SWAGGER_URL = os.getenv("SWAGGER_URL", "/docs")
    API_URL = os.getenv("API_URL", "/static/swagger.json")
