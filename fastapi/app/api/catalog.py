from fastapi import APIRouter
from .routes import food

api_router = APIRouter()
api_router.include_router(
    food.router, prefix="/food", tags=["food"])