# app/ingestion/loaders/base_loader.py

from abc import ABC, abstractmethod


class BaseLoader(ABC):

    @abstractmethod
    def extract_text(self) -> str:
        pass