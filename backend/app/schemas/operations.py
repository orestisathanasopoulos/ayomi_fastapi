from typing import Optional
from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
import re


class Operation(BaseModel):
    operation:str
    @field_validator('operation')
    @classmethod
    def check_format(cls,v:str) -> str:
        operation_no_spaces=v.strip().replace(" ", "")
        pattern = r'(\d+(?:\.\d+)?)+(?:\+|-|\*|\*\*|\/)+'
        if not re.fullmatch(pattern,operation_no_spaces):
            raise ValueError("Format Error - the operation must consist of numbers followed by operators")
        return v    
    
class OperationWithResultBase(Operation):
    result :int|float

class CreateOperationWithResult(Operation):
    result:float|int

class OperationWithResultInDb(OperationWithResultBase):
    id:int
    time_created:datetime
    time_updated:Optional[datetime]
         
    model_config = ConfigDict(
        from_attributes= True
    )



re.fullmatch