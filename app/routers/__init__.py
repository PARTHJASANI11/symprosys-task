from fastapi import APIRouter
from app.routers.token_generation import api_router as token_generation_routes
from app.routers.products import api_router as products_routes
api_router = APIRouter(prefix="/api")

api_router.include_router(
    token_generation_routes,
)
api_router.include_router(products_routes)

@api_router.get("/ping", tags=["Health Check"])
def ping():
    return {"ping": "pong"}