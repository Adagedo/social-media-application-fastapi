from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .. import schema
from .. import model, Oauth2

router = APIRouter(
    tags=["vote"]
)

@router.post("/votes", status_code=status.HTTP_201_CREATED)
async def Votes(vote_schema:schema.Vote, db:Session=Depends(get_db), current_user:int=Depends(Oauth2.get_current_user)):
    vote_query = db.query(model.Vote).filter(model.Vote.post_id == vote_schema.post_id, model.Vote.user_id == current_user._id)
    found_vote = vote_query.first()
    if vote_schema._dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="cant vote twice")
        new_vote = model.Vote(post_id=vote_schema.post_id, user_id = current_user._id)
        db.add(new_vote)
        db.commit()
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="vote not found")
        
    pass
 