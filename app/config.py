# app/config.py
import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
    CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "papers")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
    MAX_CHUNK_SIZE = 500