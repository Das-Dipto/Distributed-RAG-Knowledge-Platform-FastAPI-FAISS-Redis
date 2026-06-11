# app/ingestion/loaders/loader_factory.py

from pathlib import Path

from app.ingestion.loaders.txt_loader import TXTLoader


class LoaderFactory:

    @staticmethod
    def get_loader(file_path: str):
        suffix = Path(file_path).suffix.lower()

        if suffix == ".txt":
            return TXTLoader(file_path)

        raise ValueError(f"Unsupported file type: {suffix}")