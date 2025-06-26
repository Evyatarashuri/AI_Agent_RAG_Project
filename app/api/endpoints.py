# app/api/endpoints.py
from flask import Blueprint, request, jsonify
from app.utils.pdf_processor import process_pdf_files
from app.rag.chain import run_rag_pipeline
from app.models import QueryRequest
from pydantic import ValidationError

api_bp = Blueprint("api", __name__)

# --- Upload PDFs ---
@api_bp.route("/papers", methods=["POST"])
def upload_papers():
    if 'files' not in request.files:
        return jsonify({"error": "No files part in the request"}), 400

    files = request.files.getlist("files")

    if not files:
        return jsonify({"error": "No files provided"}), 400

    document_ids = process_pdf_files(files)

    return jsonify({
        "message": "PDFs processed successfully",
        "document_ids": document_ids
    }), 200


@api_bp.route("/query", methods=["POST"])
def query_documents():
    data = request.get_json()
    try:
        query_req = QueryRequest(**data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    result = run_rag_pipeline(query_req.question)
    return jsonify(result), 200
