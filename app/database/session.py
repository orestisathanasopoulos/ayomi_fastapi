from sqlalchemy import create_engine
from app.database.config import Settings
from sqlalchemy.orm import sessionmaker

settings = Settings()

engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# "postgresql+psycopg2://postgres:postgres@localhost:5432/fast_test"