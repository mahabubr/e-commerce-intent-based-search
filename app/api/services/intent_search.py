import faiss
import os
from app.models.embedding import embedding
from app.models.query import query
import pandas as pd
from app.logger.search_logger import search_logger
from app.models.ranking import ranking
import time

index_path = os.getcwd() + "/app/database/products_vector.bin"
index = faiss.read_index(index_path)


products_path = os.getcwd() + "/app/datasets/products.csv"
products = pd.read_csv(products_path)


def perform_intent_search(search):
    start_time = time.time()

    refine_search = query(search)

    search_embed = embedding(refine_search)

    top_k = 10
    distance, indices = index.search(search_embed, top_k)

    results = products.iloc[indices[0]].to_dict(orient="records")

    ranking_product = ranking(refine_search, results)

    execution_time = time.time() - start_time

    search_logger(search, refine_search, distance[0].tolist(), execution_time)

    return {
        "message": "Intent Search Completed",
        "data": ranking_product,
        "indices": indices[0].tolist(),
        "distances": distance[0].tolist(),
    }
