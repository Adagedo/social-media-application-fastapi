from fastapi import status
from pydantic import BaseModel


class ValidationErrorResponse(BaseModel):
    status_code:int = status.HTTP_422_UNPROCESSABLE_ENTITY
    message:str = "validation error"
    error:list
    
class ErrorResponse(BaseModel):
    status_code:int 
    message:str
    