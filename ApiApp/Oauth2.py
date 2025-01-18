from jose import jwt, JWTError
from datetime import datetime, timedelta
from . import schema
from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from .db import get_db
from . import model
from .config import settings
# secreate key algorithms, expiration date

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expires_minutes)
    to_encode.update({"exp":expire})
    token= jwt.encode(to_encode, settings.secrete_key, algorithm=settings.algorithm)
    return token


def verify_access_token(token:str, credential_exceptions):
    try:
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="user is not authenticated please sigin to use this route")
        payload = jwt.decode(token, settings.secrete_key, algorithms=[settings.algorithm])
        _id:str = payload.get("user_id")
        if not _id :
            raise credential_exceptions
        token_data = schema.TokenData._id = _id
    except JWTError:
        raise credential_exceptions
    
    return token_data

async def GetCookie(request:Request):
    try:
        cookie = request.cookies.get("my_cookie")
        return cookie
    except Exception as error:
        print(error)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorised user")
    
    
def get_current_user(token:str=Depends(GetCookie), db:Session=Depends(get_db)):
    credential_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="not authenticated!!!",headers={"www-Authenticate":"Bearer"})
    user_id =  verify_access_token(token, credential_exceptions)
    user = db.query(model.User).filter(model.User._id == user_id).first()
    return user
    

