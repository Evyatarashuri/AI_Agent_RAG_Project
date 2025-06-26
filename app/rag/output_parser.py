import re

def parse_llm_output(text: str) -> dict:
    sources = re.findall(r'\[source:\s*(.*?)\]', text)
    cleaned = re.sub(r'\[source:.*?\]', '', text).strip()
    return {
        "answer": cleaned,
        "sources": list(set(sources))
    }
