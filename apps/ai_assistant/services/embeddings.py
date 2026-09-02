from sentence_transformers import SentenceTransformer


_model = None


def get_embedding_model():
    global _model

    if _model is None:
        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _model


def generate_embedding(text: str) -> list[float]:
    model = get_embedding_model()

    embedding = model.encode(text)

    return embedding.tolist()


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    model = get_embedding_model()

    embeddings = model.encode(texts)

    return embeddings.tolist()