from datetime import date
from typing import Generator, List
from fastapi import FastAPI,HTTPException,Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import select,insert
import uvicorn
import pandas as pd
import os  
from app.database.session import SessionLocal
from app.schemas.operations import Operation,OperationWithResultInDb,CreateOperationWithResult
from app.database.models import OperationWithResult

from app.calculator import postfixEval


app =  FastAPI()


def get_db() -> Generator:
    db = SessionLocal()  
    try:
        yield db  
    finally:
        db.close() 


@app.get('/test')
async def test():
    return {"Hi":"I'm here"}

@app.post('/calculate',status_code=201, response_model=OperationWithResultInDb)
def calculate(request:Operation,db: Session = Depends(get_db)):
    calculation = postfixEval(request.operation)
    print("RESULT",calculation)
    complete_operation:CreateOperationWithResult = {"operation":request.operation,"result":calculation}
    new_row = OperationWithResult(operation=request.operation,result=calculation)
    print(new_row.id)
    db.add(new_row)
    db.commit()
    db.refresh(new_row)
    return new_row


@app.get('/data',status_code=200,response_model=List[OperationWithResultInDb])
def fetchOperation(
    db: Session = Depends(get_db)):
    results = db.execute(select(OperationWithResult).order_by(OperationWithResult.id))
    
    if not results:
        raise HTTPException(
            status_code=404, detail="Operations not found"
        )
   
    os.makedirs('./outputs', exist_ok=True)  
    json_results = jsonable_encoder(results.scalars().all())    
    df = pd.DataFrame(json_results)
    df.to_csv(f'./outputs/out{date.today()}.csv',index=False)  
        
    return results.scalars().all()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)