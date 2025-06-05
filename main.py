from fastapi import FastAPI 
from pydantic_settings import BaseSettings
from fastapi.middleware.cors import CORSMiddleware
from api.Social.utils.database import Base, engine
from api.Social.routers.auth import auth_router
from api.Social.routers.comments import comment_router
from api.Social.routers.users import users_router
from api.Social.routers.posts import posts_router
from api.Social.routers.notification import notifications_router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)




@app.get("/")
async def root():
    return "server is runinning"


