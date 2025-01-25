from datetime import timedelta, datetime
from jose import jwt, JWTError
from ApiApp.config import settings
from ApiApp.schema import TokenData
from fastapi import Response, Request, HTTPException, status, Depends

SECRETE = "..."

def Create_token(data:dict):
    to_encode = data.copy()
    exprire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp":settings.access_token_expires_minutes})
    token = jwt.encode(to_encode, settings.secrete_key, algorithm=settings.algorithm)
    return token

def verify(token, credentailException):
    payload = jwt.decode(token,settings.secrete_key, algorithms=[settings.algorithms])
    try: 
        _id = payload.get("user_id")
        if not _id:
            raise credentailException
        token_data = TokenData._id = _id
    except JWTError:
        raise credentailException
    return token_data


def GetCookies(request:Request):
    try:
        cookies_data = request.get_cookie("my_cookies")
        return cookies_data
    except Exception:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="forbbiden")

def get_current_user(token:str=Depends(GetCookies)):
    credential_Exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthoried", headers={"Bearer":"www-Authenticate"})
    current_user = verify(token, credential_Exception)
    return current_user
    
        
    
        
    