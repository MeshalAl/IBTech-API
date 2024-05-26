from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.database import get_session
from resources.products.product_service import ProductService
from resources.products.product_schema import ProductCreate, ProductUpdate, ProductResponse
from core.deps import get_current_active_admin
from core.error_handlers import HTTPError
from typing import Sequence

router = APIRouter()


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED,
             responses={
                 400: {"description": "Bad Request", "model": HTTPError},
                 401: {"description": "Unauthorized", "model": HTTPError},
                 403: {"description": "Forbidden", "model": HTTPError},
                 422: {"description": "Validation Error", "model": HTTPError},
                 500: {"description": "Internal Server Error", "model": HTTPError}
             })
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_session),
    current_user=Depends(get_current_active_admin)
):
    service = ProductService(db)
    return service.create_product(product)


@router.get("/", response_model=List[ProductResponse],
            responses={
    400: {"description": "Bad Request", "model": HTTPError},
    404: {"description": "Not Found", "model": HTTPError}
})
def read_products(skip: int = 0,
                  limit: int = 10,
                  min_price: float | None = None,
                  max_price: float | None = None,
                  category: str | None = None,
                  db: Session = Depends(get_session)) -> Sequence[ProductResponse]:
    service = ProductService(db)
    return service.get_products(skip, limit, min_price, max_price, category)


@router.get("/{product_id}", response_model=ProductResponse,
            responses={
                400: {"description": "Bad Request", "model": HTTPError},
                404: {"description": "Not Found", "model": HTTPError},
                422: {"description": "Validation Error", "model": HTTPError}
            }
            )
def read_product(product_id: int, db: Session = Depends(get_session)) -> ProductResponse:
    service = ProductService(db)
    db_product = service.get_product(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/{product_id}", response_model=ProductResponse,
            responses={
                400: {"description": "Bad Request", "model": HTTPError},
                401: {"description": "Unauthorized", "model": HTTPError},
                403: {"description": "Forbidden", "model": HTTPError},
                404: {"description": "Not Found", "model": HTTPError},
                422: {"description": "Validation Error", "model": HTTPError},
                500: {"description": "Internal Server Error", "model": HTTPError}
            })
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_session),
    current_user=Depends(get_current_active_admin)
) -> Sequence[ProductResponse]:
    service = ProductService(db)
    db_product = service.update_product(product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/{product_id}", response_model=ProductResponse,
               responses={
                   400: {"description": "Bad Request", "model": HTTPError},
                   401: {"description": "Unauthorized", "model": HTTPError},
                   403: {"description": "Forbidden", "model": HTTPError},
                   404: {"description": "Not Found", "model": HTTPError},
                   422: {"description": "Validation Error", "model": HTTPError},
                   500: {"description": "Internal Server Error", "model": HTTPError}
               })
def delete_product(product_id: int, db: Session = Depends(get_session),
                   current_user=Depends(get_current_active_admin)
                   ):
    service = ProductService(db)
    db_product = service.delete_product(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
