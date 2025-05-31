from fastapi import APIRouter
from api.v1.routers.auth import auth
from api.v1.routers.comments import commment
from api.v1.routers.posts import posts
from api.v1.routers.notification import notification
from api.v1.routers.users import users

version_one = APIRouter(prefix="/api/v1")

version_one.include_router(auth)
version_one.include_router(commment)
version_one.include_router(posts)
version_one.include_router(notification)
version_one.include_router(users)