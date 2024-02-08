from datetime import date
from typing import Generator, List
from fastapi import FastAPI,HTTPException,Depends, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import select,insert
import uvicorn
import pandas as pd
import os  
from app.database.session import SessionLocal
from app.schemas.operations import Operation,OperationWithResultInDb,CreateOperationWithResult
from app.database.models import OperationWithResult

from app.calculator import postfixEval
from dotenv import load_dotenv
load_dotenv()

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


@app.get('/data',status_code=200,response_class=FileResponse)
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
    filename = f'out{date.today()}.csv'
    path = f'./outputs/out{date.today()}.csv'
    if not path:
        raise HTTPException(status_code=404,detail="File not found")
    headers = {'Content-Disposition': 'attachment; '}
    return path
    
    # return results.scalars().all()


app.mount("/", StaticFiles(directory=os.getenv("PATH_TO_BUILD"),html = True), name="static")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)