# README.md

# 🧠 AI Academic Research Assistant

An intelligent agent that answers questions based on user-uploaded academic PDFs using Retrieval-Augmented Generation (RAG) and a locally hosted LLM via Ollama.

---

## 🚀 Features

- 📄 Upload and analyze multiple research PDFs
- 🔍 Semantic search over document content
- 🤖 Generate context-aware answers with source citations
- 🧠 Local LLM powered by Ollama (e.g. LLaMA2, Mistral)
- 📦 Fully containerized with Docker and Docker Compose
- 📝 Interactive API docs via Swagger
- 🧾 MongoDB-based query logging with metadata

---

## ⚙️ Tech Stack

| Component         | Tech Used            |
|------------------|----------------------|
| Backend API       | Flask + Pydantic     |
| Vector Database   | ChromaDB             |
| Embeddings        | nomic-embed-text / Ollama |
| Language Model    | Ollama (LLaMA2, etc) |
| Storage & Logs    | MongoDB + Mongo Express |
| Containerization  | Docker, Docker Compose |
| Docs UI           | Swagger/OpenAPI      |

---

## 📁 Project Structure

```bash
project_root/
├── docker-compose.yml
├── Dockerfile
├── modelfile/
│   └── Modelfile
├── static/
│   └── swagger.json
├── app/
│   ├── main.py
│   ├── config.py
│   ├── api/
│   ├── utils/
│   ├── database/
│   └── rag/
├── requirements.txt
├── .env
└── README.md
```

---

## 🧪 Quick Start (Local with Docker)

```bash
# 1. Build and start all services
$ docker-compose up --build

# 2. Visit the API:
#    - POST /papers (upload PDFs)
#    - POST /query  (ask questions)
#    - GET  /docs   (Swagger UI)
```

---

## 📌 Status
✅ Core functionality complete: upload → embed → query → answer → log.
🛠 In progress: refining Swagger UI and adding test coverage.

---
