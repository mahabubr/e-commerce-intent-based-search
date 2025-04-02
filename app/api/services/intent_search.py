import faiss
import os
from app.models.embedding import embedding
from app.models.query import query
import pandas as pd
from app.logger.search_logger import search_logger
import time

index_path = os.getcwd() + "/app/database/products_vector.bin"
index = faiss.read_index(index_path)


products_path = os.getcwd() + "/app/datasets/products.csv"
products = pd.read_csv(products_path)


def perform_intent_search(search):
    start_time = time.time()

    refineSearch = query(search)

    search_embed = embedding(refineSearch)

    top_k = 10
    distance, indices = index.search(search_embed, top_k)

    results = products.iloc[indices[0]].to_dict(orient="records")

    execution_time = time.time() - start_time

    refineSearch = search_logger(
        search, refineSearch, distance[0].tolist(), execution_time
    )

    return {
        "message": "Intent Search Completed",
        "data": results,
        "indices": indices[0].tolist(),
        "distances": distance[0].tolist(),
    }
