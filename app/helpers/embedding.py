from sentence_transformers import SentenceTransformer

model_name = "all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)


def embedding(text):
    if isinstance(text, str):
        text = [text]

    embedding = model.encode(
        text,
        batch_size=256,
        show_progress_bar=True,
    )

    return embedding
