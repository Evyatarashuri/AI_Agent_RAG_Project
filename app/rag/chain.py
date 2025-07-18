import time
import httpx
import logging
from app.utils.embeddings import get_embedding
from app.database.chroma_client import query_chroma
from app.database.mongo_client import log_query
from app.config import Config
from app.utils.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = "You are an academic assistant. Answer the question based on the provided context. Cite sources."


def format_prompt(context: list[str], question: str) -> str:
    joined_context = "\n\n".join(context)
    return f"{SYSTEM_PROMPT}\n\nContext:\n{joined_context}\n\nQuestion: {question}\nAnswer:"


def run_rag_pipeline(question: str):
    start = time.time()
    logger.info("Start to run RAG pipeline")

    embedding = get_embedding(question)
    logger.info("Embedding successful")

    results = query_chroma(embedding)
    logger.info("ChromaDB query successful")

    contexts = results["documents"][0]
    metadatas = results["metadatas"][0]

    prompt = format_prompt(contexts, question)
    logger.info(f"Prompt formatted:\n{prompt}")

    response = httpx.post(
        f"{Config.OLLAMA_URL}/api/generate",
        json={
            "model": Config.CHAT_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120.0
    )

    response.raise_for_status()
    answer = response.json()["response"].strip()

    end = time.time()
    duration = round(end - start, 3)
    logger.info(f"Response received successfully in {duration} seconds")

    log_query(
        question=question,
        contexts=contexts,
        answer=answer,
        sources=[meta["source"] for meta in metadatas],
        metadata={"duration_sec": duration}
    )

    return {
        "answer": answer,
        "sources": [meta["source"] for meta in metadatas]
    }
