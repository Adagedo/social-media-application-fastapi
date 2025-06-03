from fastapi import APIRouter, status, Depends, Response
from api.Social.schemas.user import (
    CreateUserSchema, 
    User, UserCreateResponse, 
    UserLoginS, 
    UserLoginSchema, 
    UserResponse, 
    UserUpdateSchema
)
from api.Social.response.success_response import success_response
from sqlalchemy.orm import Session
from api.Social.utils.dependecies import get_db
from api.Social.services.user import user_service 

auth_router = APIRouter(prefix="/auth", tags=["auth"])

#login routes 

@auth_router.post("/register", status_code = status.HTTP_201_CREATED)
async def registerUser(user:CreateUserSchema, db:Session = Depends(get_db)) -> dict:
    
    data = user_service.create_user(user=user, db=db)
    
    response = {
        "data":data, 
        "message":"Account created successfully!"
    }
    
    return response 

@auth_router.post(
    "/login", status_code = status.HTTP_202_ACCEPTED
)
async def loginUser(user:UserLoginS, db:Session = Depends(get_db))-> dict:
    
    data = user_service.handel_user_login(userLogin=user, db=db)
    
    response = {
        "message":"user login successfully",
        "data":data
    }
    
    return response 

@auth_router.get("/logout")
async def LogOut(response:Response):
    response.set_cookie(key="my_cookie", value="token strings to expires soon", max_age=1, httponly=True, secure=False)
    return "user logout!!!"