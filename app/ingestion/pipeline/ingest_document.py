from pathlib import Path

from app.ingestion.loaders.loader_factory import LoaderFactory
from app.ingestion.chunking.text_chunker import TextChunker


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

    chunker = TextChunker(
        chunk_size=500,
        overlap=50
    )

    chunks = chunker.chunk(
        text=extracted_text,
        document_id=document_id
    )

    print(f"Total Chunks Created: {len(chunks)}")

    for chunk in chunks[:3]:

        print("-" * 50)

        print(f"Chunk Index: {chunk.chunk_index}")
        print(f"Chunk ID: {chunk.chunk_id}")
        print(f"Chunk Length: {len(chunk.text)}")

        print("Chunk Preview:")
        print(chunk.text[:150])

    print("DOCUMENT INGESTION FINISHED")
    print("=" * 50)