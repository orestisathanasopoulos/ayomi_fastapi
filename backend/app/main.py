from datetime import date
from typing import Generator
from fastapi import FastAPI,HTTPException,Depends, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import select
import uvicorn
import pandas as pd
import os  
from app.database.session import SessionLocal
from app.schemas.operations import Operation,OperationWithResultInDb,CreateOperationWithResult
from app.database.models import OperationWithResult

from app.calculator import postfixEval
from dotenv import load_dotenv
load_dotenv()

app =  FastAPI(
    title="Test RPN calculator app",
    summary="An app that calculates operations using postfix notation",
    version="0.0.1",
    contact={
        "name":"Orestis Athanasopoulos",
        "email":"orestisaath@me.com"
        }
)



origins = [
    "http://localhost:4173",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db() -> Generator:
    db = SessionLocal()  
    try:
        yield db  
    finally:
        db.close() 


@app.get('/test', deprecated=True)
async def test():
    return {"Hi":"I'm here"}

@app.post('/calculate',status_code=201, response_model=OperationWithResultInDb,response_description="The created operation with result record")
def calculate(request:Operation,db: Session = Depends(get_db)):
    """
    Creates a new operation/result record:
    - **operation**: operation string written in Reverse Polish Notation (postfix notation) - REQUIRED (Example string: 3 5 +)
    - **result**: the result of the operation (validated against a pydantic schema)
   
    """
    calculation = postfixEval(request.operation)
    new_row = OperationWithResult(operation=request.operation,result=calculation)
    db.add(new_row)
    db.commit()
    db.refresh(new_row)
    return new_row


@app.get('/data',status_code=200,response_class=FileResponse, response_description="All operation with results records in a CSV file")
def fetchOperation(
    db: Session = Depends(get_db)):
    """
    Writes and downloads all records from the database in a CSV file using pandas
    """
    results = db.execute(select(OperationWithResult).order_by(OperationWithResult.id))
    
    if not results:
        raise HTTPException(
            status_code=404, detail="Operations not found"
        )
   
    os.makedirs('./outputs', exist_ok=True)  
    json_results = jsonable_encoder(results.scalars().all())     
    df = pd.DataFrame(json_results)
    df.to_csv(f'./outputs/out{date.today()}.csv',index=False)  
    path = f'./outputs/out{date.today()}.csv'
    if not path:
        raise HTTPException(status_code=404,detail="File not found")
    return path
    



if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)