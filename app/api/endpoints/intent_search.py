from fastapi import APIRouter
from ..services.intent_search import perform_intent_search

router = APIRouter()


@router.post("/intent-search")
async def intent_search():
    result = perform_intent_search()

    return result
