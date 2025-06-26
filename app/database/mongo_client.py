from pymongo import MongoClient
from datetime import datetime
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client["ai_agent"]
collection = db["query_logs"]

def log_query(question, contexts, answer, sources, metadata=None):
    entry = {
        "timestamp": datetime.utcnow(),
        "question": question,
        "contexts": contexts,
        "answer": answer,
        "sources": sources,
        "metadata": metadata or {}
    }
    collection.insert_one(entry)
