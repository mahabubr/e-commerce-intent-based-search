from fastapi import FastAPI
from .api.endpoints import search

app = FastAPI()

app.include_router(search.router)


@app.get("/")
def intent_search():
    return {"message": "Welcome To E-Commerce Intent Search..."}
