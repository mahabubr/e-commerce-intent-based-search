from fastapi import FastAPI
from .api.endpoints import intent_search

app = FastAPI()

app.include_router(intent_search.router)


@app.get("/")
def intent_search():
    return {"message": "Welcome To E-Commerce Intent Search..."}
