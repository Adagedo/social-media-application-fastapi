from fastapi import APIRouter, Depends, status, WebSocket, WebSocketDisconnect, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from api.Social.models.user import User

from api.Social.schemas.posts import (CreatePostSchema, UpdatePostSchema, RePostCreate, RepostResponse)
from api.Social.utils.dependecies import get_db
from api.Social.utils.websocket import manager
from api.Social.services.user import user_service
from api.Social.services.post import post_service

posts_router = APIRouter(prefix="posts", tags=["posts"])




@posts_router.get("", response_model=List[RepostResponse], status_code=status.HTTP_200_OK)
async def get_feeds(
        db: Session = Depends(get_db),
        user: User = Depends(user_service.get_current_user_validation),):

    feeds = post_service.get_feeds(db=db, user=user)

    response =  {
            "message":"Feeds returned successfully",
            "data":feeds
    }
    
    return response  


@posts_router.post("", status_code=status.HTTP_201_CREATED)
async def create_post(
    post: CreatePostSchema,
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_user_validation),
):
    new_post = post_service.create(db=db, user=user, schema=post)

    manager.broadcast(new_post)

    response = { 
        "message":"Post created successfully",
        "data":new_post,
    }
    
    return response

@posts_router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    id: str,
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_user_validation),
):
    post_service.delete(db=db, user=user, post_id=id)
    
    response = {
         "message":"Post deleted successfully"
    }
    
    return response 


@posts_router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_post(
    id: str,
    schema: UpdatePostSchema,
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_user_validation),
):
    updated_post = post_service.update(db=db, user=user, post_id=id, schema=schema)

    manager.broadcast(updated_post)

    response= {
        "message":"Post updated successfully"
    }
    
    return response

posts_router.websocket("/wes")
async def websocket_post_endpoint(websocket:WebSocket):
    
    await manager.connect(websocket=websocket)
    
    try:
        
        while True:
            await websocket.send_text("connected")
            await websocket.receive_text()
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        
        
@posts_router.patch("/{id}/like", status_code=status.HTTP_200_OK)
async def like_post(
    id: str,
    background_task: BackgroundTasks = BackgroundTasks(),
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_user_validation),
):
    post_service.like_post(db=db, user=user, post_id=id, background_task=background_task)
    
    response = {
        "message":"successfully liked a post", 
    }
    
    return response 


@posts_router.get("/{id}/like", status_code=status.HTTP_200_OK)
async def get_likes(
    id: str,
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_user_validation),
):

    likes = post_service.get_likes(db=db, post_id=id, user=user)
    
    response = {
        "message":"Likes returned successfully",
        "data":likes
    }
    
    return response
  

@posts_router.post("/{id}/repost", status_code=status.HTTP_201_CREATED)
async def repost(
    id: str,
    schema: RePostCreate,
    background_task: BackgroundTasks = BackgroundTasks(),
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_user_validation),
):

    repost = post_service.repost(db=db, post_id=id, schema=schema, user=user, background_task=background_task)

    manager.broadcast(repost)
    
    response = {
        "message":"repost successfully", 
        "data":repost
    }
    return response

