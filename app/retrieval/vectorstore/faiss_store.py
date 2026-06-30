from pathlib import Path

import faiss
import numpy as np


class FAISSStore:

    def __init__(
        self,
        dimension: int,
        index_path: str = "data/faiss/vector.index"
    ):
        self.dimension = dimension
        self.index_path = Path(index_path)

        self.index = self._load_or_create_index()

    def _load_or_create_index(self):

        if self.index_path.exists():
            print("Loading existing FAISS index...")

            return faiss.read_index(
                str(self.index_path)
            )

        print("Creating new FAISS index...")

        return faiss.IndexFlatL2(
            self.dimension
        )

    def add_embeddings(
        self,
        embeddings
    ):

        vectors = np.asarray(
            embeddings,
            dtype=np.float32
        )

        self.index.add(vectors)

    def save(self):

        self.index_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            str(self.index_path)
        )

    def total_vectors(self):

        return self.index.ntotal