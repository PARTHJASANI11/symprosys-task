from fastapi import FastAPI

from app.routers import api_router

app = FastAPI(
    title="Symprosys Task",
    description="Symprosys Task",
    version="0.1.0",
)

app.include_router(api_router)