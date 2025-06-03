from fastapi import APIRouter, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session
from api.Social.schemas.post_comments import CreateCommentSchema, CommentResponse
from api.Social.schemas.user import UserResponse
from api.Social.services.post_comments import comment_service
from api.Social.utils.dependecies import get_db
from api.Social.services.user import user_service
from api.Social.services.post import post_service
from api.Social.models.user import User
from api.Social.models.post import Post


comment_router = APIRouter(prefix="/post/{post_id}", tags=["comment"])

@comment_router.get("/comments")
async def getComments(post_id:str, user:User=Depends(user_service.get_current_user_validation), db:Session=Depends(get_db)):
    user_comments = comment_service.get_comments(db=db, user=user, post_id=post_id)
    
    response = {
        "message":"comments returned!!!", 
        "comment":user_comments
    }
    return response


@comment_router.post("/comments", status_code=status.HTTP_201_CREATED)
async def createComment(
    post_id:str, 
    comment:CreateCommentSchema, 
    background_task:BackgroundTasks=BackgroundTasks(),
    db:Session=Depends(get_db), 
    user:User= Depends(user_service.get_current_user_validation),
):
    new_comment:CommentResponse = comment_service.create(
        post_id=post_id, 
        user=user, 
        schema=comment, 
        background_task=background_task, 
        db=db
    )
    
    response = {
        "message":"comment created!!!", 
        "new_comments":new_comment
    }
    
    return response 

@comment_router.put("/comments/{comment_id}", status_code=status.HTTP_201_CREATED)
async def updateComment(
    post_id: str,
    comment_id: str,
    comment: CreateCommentSchema,
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_user_validation)
):
    updated_comment = comment_service.update(
        post_id=post_id, 
        comment_id=comment_id, 
        comment=comment, 
        db=db,
        user=user
    )

    response = {
        "message":"comment updated!!!", 
        "new_comment":updated_comment
    }
    
    return response


@comment_router.delete("/comments/{comment_id}", status_code = status.HTTP_204_NO_CONTENT)
async def deleteComment(
    post_id: str,
    comment_id: str,
    user: User = Depends(user_service.get_current_user),
    db: Session = Depends(get_db), 
    
):
    comment_service.delete(db=db, user=user, post_id=post_id, comment_id=comment_id)
    
    response = {
        "message": "Comment deleted successfully"
    }
    
    return response



