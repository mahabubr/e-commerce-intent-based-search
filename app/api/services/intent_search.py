import faiss
import os
from app.helpers.embedding import embedding
import pandas as pd

index_path = os.getcwd() + "/app/database/products_vector.bin"
index = faiss.read_index(index_path)


products_path = os.getcwd() + "/app/datasets/products.csv"
products = pd.read_csv(products_path)


def perform_intent_search(search):
    search_embed = embedding(search)

    top_k = 10
    distance, indices = index.search(search_embed, top_k)

    results = products.iloc[indices[0]].to_dict(orient="records")

    return {
        "message": "Intent Search Completed",
        "data": results,
        "indices": indices[0].tolist(),
        "distances": distance[0].tolist(),
    }
