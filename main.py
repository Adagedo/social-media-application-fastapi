from fastapi import FastAPI 
from ApiApp import model
from ApiApp.db import engine
from ApiApp.routers import posts, users, order, auth
from pydantic_settings import BaseSettings
from ApiApp.config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(order.router)
app.include_router(auth.router)
model.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return "server is runinning"


