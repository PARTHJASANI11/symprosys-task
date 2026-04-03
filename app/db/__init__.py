from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import DATABASE_URL

database_engine = create_engine(
    url=DATABASE_URL
    )
session_maker = sessionmaker(bind=database_engine)

def get_database_session():
    session_local = session_maker()
    try:
        yield session_local
    finally:
        session_local.close()