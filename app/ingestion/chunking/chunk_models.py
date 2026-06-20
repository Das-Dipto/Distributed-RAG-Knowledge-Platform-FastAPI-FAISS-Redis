from dataclasses import dataclass


@dataclass
class TextChunk:
    chunk_id: str
    document_id: str
    text: str
    chunk_index: int
    embedding: list | None = None