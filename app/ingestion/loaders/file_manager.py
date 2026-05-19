from pathlib import Path
from uuid import uuid4
import shutil


UPLOAD_DIR = Path("data/uploads")


class FileManager:
    @staticmethod
    def generate_document_id() -> str:
        return f"doc_{uuid4().hex[:8]}"

    @staticmethod
    def save_uploaded_file(file, document_id: str) -> str:
        suffix = Path(file.filename).suffix

        filename = f"{document_id}{suffix}"

        save_path = UPLOAD_DIR / filename

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return str(save_path)