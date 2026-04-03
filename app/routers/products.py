from fastapi import APIRouter, Depends
from app.db import get_database_session
from app.core import task_logger
from app.db.db_service import DBService
from app.schemas.products import (
    CreateProductCategoryRequest, CreateProductCategoryResponse, CreateProductRequest,
    CreateProductResponse,
    )

api_router = APIRouter()


@api_router.post("/v1/product-category", tags=["Products"], response_model=CreateProductCategoryResponse)
def create_product_category(product_category: CreateProductCategoryRequest, db_session = Depends(get_database_session)):
    try:
        product_category = product_category.name
        db_service = DBService(db_session)
        added_product_category = db_service.add_product_category(product_category)
        return {"id": added_product_category.id, "category": added_product_category.name}

    except Exception as e:
        task_logger.exception(e)

@api_router.post("/v1/product", tags=["Products"], response_model=CreateProductResponse)
def generate_token(product_data: CreateProductRequest, db_session = Depends(get_database_session)):
    try:
        product_data = product_data
        db_service = DBService(db_session)
        added_product = db_service.add_product(product_data)
        return {
            "id": added_product.id,
            "title": added_product.title,
            "description": added_product.description,
            "price": added_product.price,
            "status": added_product.status,
            "category": added_product.category_id,
            "created_at": added_product.created_at,
            "updated_at": added_product.updated_at,
            }
    except Exception as e:
        task_logger.exception(e)