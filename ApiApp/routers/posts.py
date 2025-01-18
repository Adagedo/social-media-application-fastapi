from .. import model, schema
from ..Oauth2 import get_current_user
from ..db import get_db
from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter()

@router.get("/posts", status_code=status.HTTP_200_OK, response_model= List[schema.PostResponse])
async def GetPosts(db:Session=Depends(get_db), user_info:int = Depends(get_current_user)):
    print(user_info._id)
    posts = db.query(model.Posts).all()
    if not posts:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post not found")
    return posts


@router.get("/posts/{id}", status_code=status.HTTP_200_OK, response_model = schema.PostResponse)
async def GetSinglePosts(id:int, db:Session=Depends(get_db), user_info:int = Depends(get_current_user)):
    print(user_info._id)
    singlePosts = db.query(model.Posts).filter(model.Posts._id == id).first()
    if not singlePosts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with the id of {id} is not found")
    
    return singlePosts


@router.post("/posts", status_code=status.HTTP_201_CREATED)
async def CreatePost(post_schema:schema.Posts, db:Session=Depends(get_db), user_info:int = Depends(get_current_user)):
    new_post = model.Posts(**post_schema.dict())
    print(user_info._id)
    new_post.owner_id = user_info._id
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return "post created!!!"


@router.delete("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def Delete(id:int, db:Session=Depends(get_db), user_info:int = Depends(get_current_user)):
    print(user_info._id)
    post_query = db.query(model.Posts).filter(model.Posts._id == id)
    if post_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with the id of {id}, can not be deleted as it does not exist")
    
    if post_query.first().owner_id != user_info._id:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="user can oonly delete his own post")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return "post deletd!!!"


@router.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def Update(id:int, post_schema:schema.UpdatePosts, db:Session=Depends(get_db), user_info:int = Depends(get_current_user)):
    print(user_info._id)
    post_query = db.query(model.Posts).filter(model.Posts._id == id)
    if post_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with the id of {id} can not updated as its not found")
    
    if post_query.first().owner_id != user_info._id:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="not allowd as user can only update his post")
    post_query.update(post_schema.dict(), synchronize_session=False)
    db.commit()
    return "Post updated!!!"   