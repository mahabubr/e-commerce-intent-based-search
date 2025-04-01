from fastapi import APIRouter
from pydantic import BaseModel
from ..services.intent_search import perform_intent_search

router = APIRouter()


class Request(BaseModel):
    search: str


@router.post("/intent-search")
async def intent_search(request: Request):
    search = request.search

    result = perform_intent_search(search)

    return result
