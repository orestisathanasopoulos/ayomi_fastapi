from datetime import date

from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient
import pandas as pd
import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database,database_exists
from .database.models import Base
from .main import app, get_db


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/calc_test"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
client = TestClient(app)
app.dependency_overrides[get_db] = override_get_db



@pytest.fixture(scope="session", autouse=True)
def test_db():
    if not database_exists(SQLALCHEMY_DATABASE_URL):
         create_database(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_read_main():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"Hi":"I'm here"}


def test_no_operations_in_db():
    response = client.get('/data')
    print(response)
    try:
        df = pd.read_csv(f'./outputs/out{date.today()}.csv')
    except:
        df = pd.DataFrame()
    assert response.status_code == 200
    assert df.empty == True

def test_create_operation():
    response = client.post(
        "/calculate",
        headers={"X-Token": "application/json"},
        json={"operation": "32 6 +"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["operation"] == "32 6 +"
    assert data["result"] == 38.0 
    
    
def test_one_operation_in_db():
    response = client.get('/data')
    assert response.status_code == 200
    try:
        df = pd.read_csv(f'./outputs/out{date.today()}.csv')
    except:
        df = pd.DataFrame()
    assert response.status_code == 200
    assert df.empty == False
    assert len(df)==1
    
    
def test_create_operation_bad_input():
    response = client.post(
        "/calculate",
        headers={"X-Token": "application/json"},
        json={"operation": "3fads2 6fad +"},
    )
    with pytest.raises(RequestValidationError):
        raise RequestValidationError("Format Error - the operation must consist of numbers followed by operators")
    assert response.status_code == 422   
    


  
    # assert response.json() == {[]}