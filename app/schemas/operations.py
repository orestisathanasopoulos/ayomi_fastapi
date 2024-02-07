from typing import Optional
from pydantic import BaseModel, ConfigDict, validator
from datetime import datetime


class Operation(BaseModel):
    operation:str
    
    
class OperationWithResultBase(Operation):
    result :int

class CreateOperationWithResult(Operation):
    result:float

class OperationWithResultInDb(OperationWithResultBase):
    id:int
    time_created:datetime
    time_updated:Optional[datetime]
         
    model_config = ConfigDict(
        from_attributes= True
    )
