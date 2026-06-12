from pypdf import PdfReader

from app.ingestion.loaders.base_loader import BaseLoader


class PDFLoader(BaseLoader):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:

        reader = PdfReader(self.file_path)

        extracted_pages = []

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                extracted_pages.append(page_text)

        return "\n".join(extracted_pages)