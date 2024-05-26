from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str | None
    description: str | None
    category: str | None
    price: float | None
    available: bool | None
    image_urls: list[str] | None

class ProductCreate(ProductBase):
    name: str
    description: str
    category: str
    price: float
    available: bool

class ProductUpdate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    category: str | None
    price: float | None
    available: bool | None
    image_urls: list[str] | None
