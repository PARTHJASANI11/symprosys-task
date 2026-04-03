from enum import Enum

from app.models import Category
from app.schemas import SchemaBaseModel


class CreateProductCategoryRequest(SchemaBaseModel):
    name: str

class CreateProductCategoryResponse(SchemaBaseModel):
    id: int
    category: str

class ProductStatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class CreateProductRequest(SchemaBaseModel):
    title: str
    description: str
    price: float
    status: ProductStatusEnum
    category_id: int

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True

class CreateProductResponse(SchemaBaseModel):
    id: int
    title: str
    description: str
    price: float
    status: ProductStatusEnum
    category_id: int