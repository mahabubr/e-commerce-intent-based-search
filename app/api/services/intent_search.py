import faiss
import os

index_path = os.getcwd() + "/app/database/products_vector.bin"

index = faiss.read_index(index_path)


def perform_intent_search(search):
    print(index)

    return {"message": "Product Get Successful", "data": []}
