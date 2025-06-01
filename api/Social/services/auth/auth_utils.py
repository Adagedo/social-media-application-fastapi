from jose import jwt, JWTError
from datetime import datatime, timedelta
from fastapi import Depends ,HTTPException, status, Request
from sqlalchemy.orm import Session
from api.Social.utils.config import settings
from api.Social.schemas.token import Token
from api.Social.schemas.user import User
from api.Social.utils.dependecies import get_db

class UserAuthenticationService():
    
    def __init__(self):
        pass
    
    def generate_access_token(self, data:dict) -> str:
        
        to_encode = data.copy()
        expire = datatime.utcnow() + timedelta(minutes=settings.access_token_expires_minutes)
        to_encode.update({"exp":expire})
        token = jwt.encode(to_encode, settings.secrete_key, algorithm=settings.algorithm)
        return token
    
    def verify_access_token(self, token:str, credential_exceptions):
        try:
            if not token:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not authenticated sigin to use this service")
            
            payload = jwt.decode(token, settings.secrete_key, algorithms=[settings.algorithm])
            _id:str = payload.get("user_id")
            if not _id:
                raise credential_exceptions
            token_data = Token._id = _id
        except JWTError as jwterror:
            raise credential_exceptions
        
        return token_data
    
    @staticmethod
    def getCookieToken(request:Request)-> str:
        
        try:
            token = request.get(settings.cookie_name)
        
        except Exception as ee:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid user")
        return token
    
    
    
    def get_current_user_validation(self, token:str=Depends(getCookieToken), db:Session=Depends(get_db)):
        
        credential_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not authenticated", headers={"www-Authenticate":"Bearer"})
        
        user_id = self.verify_access_token(token, credential_exceptions=credential_exceptions)