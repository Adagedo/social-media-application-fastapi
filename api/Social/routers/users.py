from typing import Annotated
from fastapi import APIRouter, Depends, Query, status, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from api.Social.models.user import User
from api.Social.schemas.user import UserUpdateSchema
from api.Social.services.user import user_service
from api.Social.utils.dependecies import get_db

users_router = APIRouter(prefix="/users", tags=["users"])



@users_router.put("/{user_id}", status_code = status.HTTP_200_OK)
async def updataUserProfile(updated_schema:UserUpdateSchema,user_id:str, user:User=Depends(user_service.get_current_user_validation), db:Session=Depends(get_db)):
    
    data = user_service.update_user_profile(
        user = user, 
        user_id=user_id, 
        schema=updated_schema, 
        db=db
    )
    
    response = {
        "message":"profile updated successfully", 
        "profile":data
    }
    
    return response 

@users_router.get("/{user_id}")
async def getProfilePetails(user_id:str, user:User = Depends(user_service.get_current_user_validation), db:Session = Depends(get_db)):
    
    data = user_service.get_user_details(
        user_id=user_id, 
        db=db
    )
    
    response = {
        "message":"profile data retrived", 
        "data":data
    }
    
    return response 
@users_router.delete("/{user_id}")
async def deleteUserProfile(user_id:str, db:Session = Depends(get_db), user:User = Depends(user_service.get_current_user_validation)):
    user_service.delete_user_profile(db=db, user=user, user_id=user_id)
    response = {
        "message":"account deleted successfully!!!"
    }
    
    return response 

@users_router.get("/{search}", status_code = status.HTTP_200_OK)
async def getAllUsers(search:str, db:Session=Depends(get_db)):
    
    users = user_service.fetch_all(db=db, search=search)
    
    response = {
        "message":"users retrieved successfully!!!",
        "user":users
    }
    return response 

@users_router.patch("/{followee_id}/follow")
async def follow(
    followee_id: str,
    background_task: BackgroundTasks = BackgroundTasks(),
    user: User = Depends(user_service.get_current_user_validation),
    db: Session = Depends(get_db),
):
    user_service.follow_user(
        followee_id=followee_id, 
        background_task=background_task, 
        user=user, 
        db=db
    )
    
    response = {
        "message":"user have successfully followed this user"
    }
    return response 


@users_router.delete("/{followee_id}/unfollow", status_code = status.HTTP_200_OK)
async def unfollowUser(
    followee_id: str,
    background_task: BackgroundTasks = BackgroundTasks(),
    user: User = Depends(user_service.get_current_user_validation),
    db: Session = Depends(get_db),
):
    
    user_service.unfollow_user(
        db=db, 
        background_tack=background_task,
        user=user, 
        user_id = followee_id, 
    )
    
    response = {
        "message":"you have successfully unfollowed this user"
    }
    
    return response 

@users_router.get("/{user_id}/followers", status_code = status.HTTP_200_OK)
async def getFollowers(user_id:str, user:User = Depends(user_service.get_current_user_validation), db:Session=Depends(get_db)):
    
    
    followers = user_service.followers(user=user,db=db)
    
    response = {
        "message":"successfully retrived followers", 
        "followers":followers
    }
    
    return response



@users_router.get("/{user_id}/followings", status_code = status.HTTP_200_OK)
async def followings(
    user_id: str,
    user: User = Depends(user_service.get_current_user_validation),
    db: Session = Depends(get_db),
):

    followings = user_service.followings(db=db, user=user)

    response = {
        "message":"Followings list successfully returned",
        "data":followings,
    }
    
    return response 
