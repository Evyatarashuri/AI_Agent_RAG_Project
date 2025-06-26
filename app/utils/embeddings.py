import httpx
from app.config import Config

def get_embedding(text: str) -> list:
    url = f"{Config.OLLAMA_URL}/api/embeddings"
    payload = {
        "model": Config.EMBEDDING_MODEL,
        "prompt": text
    }
    try:
        response = httpx.post(url, json=payload)
        response.raise_for_status()
        return response.json()["embedding"]
    except Exception as e:
        raise RuntimeError(f"Failed to get embedding: {e}")