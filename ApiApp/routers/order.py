from fastapi import APIRouter, status
from fastapi import HTTPException, status, Depends
from ..db import get_db
from .. import schema, model
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/order", status_code=status.HTTP_201_CREATED)
async def AddOrderController(order_schema:schema.Order, db:Session=Depends(get_db)):
    try:
        new_order = model.Order(**order_schema.dict())
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except Exception as error:
        print("error adding products", error)
    finally:
        return "products is added successfully!!!"


@router.get("/order", status_code=status.HTTP_200_OK)
async def GetProductsController(db:Session =Depends(get_db)):
    all_products = db.query(model.Order).all()
    if not all_products:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "no product found")
    return all_products


@router.get("/order/{id}", status_code = status.HTTP_200_OK)
async def GetSingleProductsController(id:int, db:Session=Depends(get_db)):
    single_products = db.query(model.Order).filter(model.Order._id == id).first()
    if not single_products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with the id of {id} is not found")
    

@router.delete("/order/{id}", status_code=status.HTTP_202_ACCEPTED)
async def DeleteController(id:int, db:Session=Depends(get_db)):
    order_query = db.query(model.Order).filter(model.Order._id == id)
    if order_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"order with the id of {id} can not be deleted as its not found")
    
    order_query.delete(synchronize_session=False)
    db.commit()
    return "order is droped successfully"


@router.put("/order/{id}", status_code = status.HTTP_202_ACCEPTED)
async def UpdateControllers(id:int, update_schema, db:Session=Depends(get_db)):
    order_query = db.query(model.Order).filter(model.Order._id == id)
    if order_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"order with the id of {id} can net be deleted as it does not exist")
    
    order_query.update(update_schema.dict(), synchronize_session=False)
    db.commit()
    return "order updated"    