from pydantic import BaseModel

class Token(BaseModel):
    
    _id:str 
    user:str