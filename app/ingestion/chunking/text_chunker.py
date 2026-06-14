from uuid import uuid4

from app.ingestion.chunking.base_chunker import BaseChunker
from app.ingestion.chunking.chunk_models import TextChunk


class TextChunker(BaseChunker):

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str, document_id: str):

        chunks = []

        start = 0
        chunk_index = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end]

            chunk = TextChunk(
                chunk_id=f"chunk_{uuid4().hex[:8]}",
                document_id=document_id,
                text=chunk_text,
                chunk_index=chunk_index
            )

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

            chunk_index += 1

        return chunks