from typing import List, Optional, Sequence
from sqlalchemy.orm import Session
from .product_dal import ProductDAL
from .product_schema import ProductCreate, ProductUpdate, ProductResponse

class ProductService:
    def __init__(self, db_session: Session):
        self.dal = ProductDAL(db_session)

    def create_product(self, product_create: ProductCreate) -> ProductResponse:
        return self.dal.create_product(product_create)

    def get_product(self, product_id: int) -> Optional[ProductResponse]:
        return self.dal.get_product(product_id)

    def get_products(self,
                     skip: int = 0,
                     limit: int = 10,
                     min_price: float | None = None,
                     max_price: float | None = None,
                     category: str | None = None
                     ) -> Sequence[ProductResponse]:
        products =  self.dal.get_products(skip, limit, min_price, max_price, category)
        if not products:
            return []
        return products

    def update_product(self, product_id: int, product_update: ProductUpdate) -> Sequence[ProductResponse]:
        return self.dal.update_product(product_id, product_update)

    def delete_product(self, product_id: int) -> Sequence[ProductResponse]:
        return self.dal.delete_product(product_id)
