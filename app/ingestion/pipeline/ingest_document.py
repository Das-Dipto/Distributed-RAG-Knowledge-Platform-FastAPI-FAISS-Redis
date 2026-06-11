# app/ingestion/pipeline/ingest_document.py

from pathlib import Path

from app.ingestion.loaders.loader_factory import LoaderFactory


def process_document_ingestion(document_id: str, file_path: str):

    print("=" * 50)
    print("DOCUMENT INGESTION STARTED")

    print(f"Document ID: {document_id}")
    print(f"File Path: {file_path}")

    file_exists = Path(file_path).exists()

    print(f"File Exists: {file_exists}")

    loader = LoaderFactory.get_loader(file_path)

    extracted_text = loader.extract_text()

    print(f"Extracted Text Length: {len(extracted_text)}")

    print("TEXT PREVIEW:")
    print(extracted_text[:300])

    print("DOCUMENT INGESTION FINISHED")
    print("=" * 50)