from fastapi import APIRouter, UploadFile, File, HTTPException

from app.ingestion.loaders.file_manager import FileManager
from app.ingestion.pipeline.ingest_document import process_document_ingestion
from app.queue.redis_queue import queue


router = APIRouter(prefix="/documents", tags=["Documents"])


ALLOWED_EXTENSIONS = {".txt", ".pdf"}


@router.post("/upload")
def upload_document(file: UploadFile = File(...)):
    suffix = file.filename[file.filename.rfind("."):].lower()

    if suffix not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only .txt and .pdf files are supported"
        )

    document_id = FileManager.generate_document_id()

    saved_file_path = FileManager.save_uploaded_file(
        file=file,
        document_id=document_id
    )

    queue.enqueue(
        process_document_ingestion,
        document_id,
        saved_file_path
    )

    return {
        "document_id": document_id,
        "status": "queued"
    }