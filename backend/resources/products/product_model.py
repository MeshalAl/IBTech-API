
from db.models.model_base import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, ARRAY, DateTime
from sqlalchemy.sql import func
from datetime import datetime


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    category = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    image_urls = Column(ARRAY(String))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
