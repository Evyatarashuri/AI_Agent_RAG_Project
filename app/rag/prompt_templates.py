SYSTEM_PROMPT = "You are an academic assistant. Answer the question based on the provided context. Cite sources."

def format_prompt(context: list[str], question: str) -> str:
    joined_context = "\n\n".join(context)
    return f"{SYSTEM_PROMPT}\n\nContext:\n{joined_context}\n\nQuestion: {question}\nAnswer:"