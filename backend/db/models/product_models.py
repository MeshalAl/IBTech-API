from database import engine
from model_base import Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)