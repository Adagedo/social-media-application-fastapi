from datetime import datetime, timedelta
from jose import jwt, JWTError
from . import schema
from fastapi import HTTPException, Depends, status, Request
from fastapi.security import OAuth2PasswordBearer

S_KEY = "......."
EX_TIME = 60
ALGO = "HS256"
OAuth_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EX_TIME)
    to_encode.update({"exp":expire})
    token = jwt.encode(to_encode, S_KEY, algorithm=ALGO)
    return token


def verify_token(token:str, credential_exception):
    try:
        payload = jwt.decode(token, S_KEY, algorithms=[ALGO])
        _id = payload.get("user_id")
        if not _id :
            raise credential_exception
        token_data = schema.Token._id = _id
    except JWTError:
        raise credential_exception
    
    return token_data

def get_current_user(token:str=Depends(OAuth_scheme)):
    credentials_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorise user", headers={"www-Authenticate":"Bearer"})
    return verify_token(token, credentials_exceptions)


def GetCookies(request:Request):
    cookies = request.cookies.get("my_cookie")
    return cookies
    

def get_current_user_with_cookies(token:str=Depends(GetCookies)):
        credentials_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorise user", headers={"www-Authenticate":"Bearer"})
        verify_token(token, credentials_exceptions)
    