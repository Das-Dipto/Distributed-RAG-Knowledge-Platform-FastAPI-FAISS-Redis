from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def generate_embeddings(self, texts: list[str]):

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings