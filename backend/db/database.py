import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

database_url = settings.database_url
print(database_url)

if not database_url:
    raise ValueError('DATABASE_URL not found in environment variables')

engine = create_engine(database_url) 
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
