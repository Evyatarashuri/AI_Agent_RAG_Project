import uuid
from PyPDF2 import PdfReader
from app.utils.embeddings import get_embedding
from app.database.chroma_client import add_to_chroma
from app.config import Config



def chunk_text(text: str, max_size: int = 1000) -> list[str]:
    """Splits text into chunks of maximum `max_size` characters."""
    return [text[i:i + max_size] for i in range(0, len(text), max_size)]


def extract_text_from_pdf(file) -> str:
    """Extracts and concatenates text from all pages of a PDF."""
    reader = PdfReader(file)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def process_pdf_files(files) -> list[str]:
    """
    Processes uploaded PDF files:
    - Extracts text
    - Splits into chunks
    - Embeds each chunk
    - Stores embeddings with metadata in ChromaDB

    Returns:
        List of document UUIDs
    """
    document_ids = []

    for file in files:
        raw_text = extract_text_from_pdf(file)
        chunks = chunk_text(raw_text, Config.MAX_CHUNK_SIZE)

        doc_id = str(uuid.uuid4())
        filename = getattr(file, "filename", "uploaded_document.pdf")

        for idx, chunk in enumerate(chunks):
            embedding = get_embedding(chunk)
            metadata = {
                "document_id": doc_id,
                "chunk_id": idx,
                "source": filename
            }
            add_to_chroma(embedding, chunk, metadata)

        document_ids.append(doc_id)

    return document_ids
