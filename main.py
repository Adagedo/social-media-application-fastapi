from fastapi import FastAPI 
from pydantic_settings import BaseSettings
from ApiApp.config import settings
from fastapi.middleware.cors import CORSMiddleware
from api.Social.utils.database import Base, engine


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return "server is runinning"


