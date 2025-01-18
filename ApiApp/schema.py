from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class Posts(BaseModel):
    title:str
    content:str
    published:str


class UpdatePosts(Posts):
    pass

class User(BaseModel):
    email:EmailStr
    password:str
    

    
class UserOut(BaseModel):
    _id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True
        


class PostResponse(BaseModel):
    owner_id:int
    title:str
    content:str
    published:str
    created_at:datetime
    owner: UserOut
    
    class Config:
        from_attributes = True



class Order(BaseModel):
    _id:int
    product:str
    price:int
    created_at:datetime

    class config:
        from_attributes = True

class LoginUser(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    token:str
    token_type: str
class TokenData(BaseModel):
    _id:Optional[str] = None

    

class Vote(BaseModel):
    post_id:int

    