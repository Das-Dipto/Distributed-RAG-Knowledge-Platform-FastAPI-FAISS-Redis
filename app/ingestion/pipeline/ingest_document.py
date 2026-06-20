from pathlib import Path

from app.ingestion.loaders.loader_factory import LoaderFactory
from app.ingestion.chunking.text_chunker import TextChunker
from app.ingestion.embedding.embedding_service import EmbeddingService


def process_document_ingestion(
    document_id: str,
    file_path: str
):
    print("=" * 50)
    print("DOCUMENT INGESTION STARTED")
    print("=" * 50)

    print(f"Document ID: {document_id}")
    print(f"File Path: {file_path}")

    if not Path(file_path).exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    # -----------------------------
    # Text Extraction Stage
    # -----------------------------
    loader = LoaderFactory.get_loader(file_path)

    extracted_text = loader.extract_text()

    print(f"Extracted Text Length: {len(extracted_text)}")

    # -----------------------------
    # Chunking Stage
    # -----------------------------
    chunker = TextChunker(
        chunk_size=500,
        overlap=50
    )

    chunks = chunker.chunk(
        text=extracted_text,
        document_id=document_id
    )

    print(f"Total Chunks Created: {len(chunks)}")

    # -----------------------------
    # Embedding Stage
    # -----------------------------
    embedding_service = EmbeddingService()

    chunk_texts = [
        chunk.text
        for chunk in chunks
    ]

    embeddings = embedding_service.generate_embeddings(
        chunk_texts
    )

    for chunk, embedding in zip(
        chunks,
        embeddings
    ):
        chunk.embedding = embedding

    print(
        f"Total Embeddings Generated: {len(embeddings)}"
    )

    print(
        f"Embedding Dimension: {len(embeddings[0])}"
    )

    # -----------------------------
    # Preview
    # -----------------------------
    for chunk in chunks[:3]:

        print("-" * 50)

        print(f"Chunk Index: {chunk.chunk_index}")
        print(f"Chunk ID: {chunk.chunk_id}")
        print(f"Chunk Length: {len(chunk.text)}")

        print("Chunk Preview:")
        print(chunk.text[:150])

    print("=" * 50)
    print("DOCUMENT INGESTION FINISHED")
    print("=" * 50)