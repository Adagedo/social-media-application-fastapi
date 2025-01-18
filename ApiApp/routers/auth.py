from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from ..db import get_db
from .. import model, schema
from sqlalchemy.orm import Session
from ..utils import verify
from ..Oauth2 import create_access_token


router = APIRouter(tags=["auths"])


@router.post("/login")
async def Login(login_schema:schema.LoginUser, response:Response, db:Session=Depends(get_db)) -> str | None:
    user = db.query(model.User).filter(model.User.email == login_schema.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    password_verification = verify(login_schema.password, user.password)
    if not password_verification:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    access_token = create_access_token(data={"user_id": user._id})
    response.set_cookie("my_cookie", access_token, max_age=3600, httponly=True, secure=False)
    
    return "login successfull"

@router.get("/logout")
async def LogOut(response:Response):
    response.set_cookie(key="my_cookie", value="token strings to expires soon", max_age=1, httponly=True, secure=False)
    return "user logout!!!"


