from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
from typing import Dict
import asyncio
from api.Social.models.user import User
from api.Social.models.notification import Notification


class NotificationService():
    
    def __init__(self):
        
        
        self.user_event_queues:Dict[str, asyncio.Queue] = {}
        
        
    async def event_generator(self, user_id:str):
        
        if user_id not in self.user_event_queues:
            self.user_event_queues[user_id] = asyncio.Queue()
            
        while True:
            event = await self.user_event_queues[user_id].get()
            yield f"data: {event}"
            
    
    def notification(self, user:User, db:Session):
        
        notifications = (
            db.query(Notification).filter(Notification.user_id == user.id).all()
        )
        
        return notifications
    
    
notification_service = NotificationService()
