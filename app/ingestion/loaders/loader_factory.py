from pathlib import Path

from app.ingestion.loaders.txt_loader import TXTLoader
from app.ingestion.loaders.pdf_loader import PDFLoader


class LoaderFactory:

    @staticmethod
    def get_loader(file_path: str):

        suffix = Path(file_path).suffix.lower()

        if suffix == ".txt":
            return TXTLoader(file_path)

        if suffix == ".pdf":
            return PDFLoader(file_path)

        raise ValueError(f"Unsupported file type: {suffix}")