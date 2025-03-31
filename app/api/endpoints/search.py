from fastapi import APIRouter
from ..services.search_service import perform_intent_search

router = APIRouter()


@router.post("/intent-search")
async def intent_search():
    result = perform_intent_search()

    return result
