import enum
from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, ForeignKey
from sqlalchemy.sql.sqltypes import Float, Enum, DateTime


class ProductStatusEnum(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(300))
    price: Mapped[Decimal] = mapped_column(Float)
    status: Mapped[ProductStatusEnum] = mapped_column(Enum(ProductStatusEnum))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)