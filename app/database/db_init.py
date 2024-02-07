from models import Base
from session import engine


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
