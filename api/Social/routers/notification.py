from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from api.Social.models.user import User
from api.Social.services.user import user_service
from api.Social.services.notification import notification_service
from api.Social.utils.dependecies import get_db
from typing import List


notifications_router = APIRouter(prefix="/notification", tages=["notification"])


@notifications_router.get("/sse")
async def sse_endpoint(user: User = Depends(user_service.get_current_user_validation)):
    return StreamingResponse(
        notification_service.event_generator(user.id), media_type="text/event_stream"
    )


@notifications_router.get("")
async def user_notifications(user: User = Depends(user_service.get_current_user_validation), db: Session = Depends(get_db)):

    notifications: List = notification_service.notifications(user=user, db=db)
    
    response = {
        "message":"Notifications returned successfully",
        "data":notifications,
    }
    
    return response 

