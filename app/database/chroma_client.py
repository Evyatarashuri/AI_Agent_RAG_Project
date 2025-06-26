import chromadb
from app.config import Config

# Initialize ChromaDB client and collection
client = chromadb.Client()
collection = client.get_or_create_collection(name=Config.CHROMA_COLLECTION_NAME)


def add_to_chroma(embedding: list[float], text: str, metadata: dict):
    """
    Adds a document chunk and its embedding to ChromaDB.

    Args:
        embedding: Vector representation of the chunk
        text: The actual chunk content
        metadata: Dictionary with source info (doc ID, chunk ID, etc.)
    """
    try:
        collection.add(
            embeddings=[embedding],
            documents=[text],
            metadatas=[metadata],
            ids=[f"{metadata['document_id']}_{metadata['chunk_id']}"]
        )
    except Exception as e:
        raise RuntimeError(f"Failed to add to ChromaDB: {e}")


def query_chroma(question_embedding: list[float], n_results: int = 5):
    """
    Queries ChromaDB for the most relevant chunks based on the question embedding.

    Args:
        question_embedding: Vector embedding of the user question
        n_results: Number of relevant chunks to retrieve

    Returns:
        Dictionary with documents and metadata
    """
    try:
        return collection.query(
            query_embeddings=[question_embedding],
            n_results=n_results,
            include=["documents", "metadatas"]
        )
    except Exception as e:
        raise RuntimeError(f"ChromaDB query failed: {e}")
