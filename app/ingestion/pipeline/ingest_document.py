from pathlib import Path


def process_document_ingestion(document_id: str, file_path: str):
    print("=" * 50)
    print("DOCUMENT INGESTION STARTED")
    print(f"Document ID: {document_id}")
    print(f"File Path: {file_path}")

    file_exists = Path(file_path).exists()

    print(f"File Exists: {file_exists}")

    print("DOCUMENT INGESTION FINISHED")
    print("=" * 50)