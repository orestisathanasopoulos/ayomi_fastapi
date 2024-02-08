import os
from models import Base
from config import Settings
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database,drop_database
print("hi")
print(os.getenv("DB_HOST"))  
settings = Settings()
engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True, echo=True)

 
if database_exists(settings.DATABASE_URI):
    drop_database(settings.DATABASE_URI)
create_database(settings.DATABASE_URI)

Base.metadata.create_all(engine)
