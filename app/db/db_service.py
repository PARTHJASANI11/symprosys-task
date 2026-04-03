from datetime import datetime

from app.models import Category, Products, ProductStatusEnum


class DBService:
    def __init__(self, session):
        self.session = session

    def add_product_category(self, category):
        category = Category(name=category)
        self.session.add(category)
        self.session.commit()
        self.session.refresh(category)
        return category

    def add_product(self, product):
        product = Products(
            title=product.title,
            description=product.description,
            price=product.price,
            status=product.status,
            category_id=product.category_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            )
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product