from sqlalchemy.orm import Session
from typing import Sequence
from .product_model import Product
from .product_schema import ProductCreate, ProductUpdate

class ProductDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_product(self, product_create: ProductCreate) -> Product:
        new_product = Product(
            name=product_create.name,
            description=product_create.description,
            category=product_create.category,
            price=product_create.price,
            available=product_create.available,
            image_urls=product_create.image_urls
        )
        self.db_session.add(new_product)
        self.db_session.flush()
        self.db_session.refresh(new_product)
        return new_product

    def get_product(self, product_id: int) -> Product | None:
        return self.db_session.query(Product).filter(Product.id == product_id).first()
    
    def get_products(self, 
                     skip: int = 0, 
                     limit: int = 10, 
                     min_price: float | None = None, 
                     max_price: float | None = None, 
                     category: str | None = None) -> Sequence[Product]:
        query = self.db_session.query(Product)
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        if max_price is not None:
            query = query.filter(Product.price <= max_price)
        if category is not None:
            query = query.filter(Product.category == category)
        return query.offset(skip).limit(limit).all()

    def update_product(self, product_id: int, product_update: ProductUpdate) -> Product | None:
        db_product = self.db_session.query(Product).filter(Product.id == product_id).first()
        if db_product:
            for key, value in product_update.model_dump(exclude_unset=True).items():
                setattr(db_product, key, value)
        self.db_session.flush()
        self.db_session.refresh(db_product)
        return db_product

    def delete_product(self, product_id: int) -> Product | None:
        db_product = self.db_session.query(Product).filter(Product.id == product_id).first()
        if db_product:
            self.db_session.delete(db_product)
        return db_product
