# app/ingestion/loaders/txt_loader.py

from pathlib import Path

from app.ingestion.loaders.base_loader import BaseLoader


class TXTLoader(BaseLoader):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        path = Path(self.file_path)

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        return text