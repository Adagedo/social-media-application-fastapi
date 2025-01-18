from .. import schema, model,utils, db
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

router = APIRouter()



@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schema.UserOut)
async def CreateUser(user_schema:schema.User, db:Session=Depends(db.get_db)):
    # hash the password of theuser
    HashedPassword = utils.Hash(user_schema.password)
    user_schema.password = HashedPassword
    new_user = model.User(**user_schema.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{id}", status_code = status.HTTP_200_OK, response_model=schema.UserOut)
async def GetSingleUser(id:int ,db:Session=Depends(db.get_db)):
    singleuser = db.query(model.User).filter(model.User._id == id).first()
    if not singleuser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user not with the id of {id}found")
    return singleuser
 