from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_username:str
    database_name:str
    database_password:str
    secrete_key:str
    algorithm:str
    access_token_expires_minutes:int
    cookie_name:str
    drivername:str
    
    class Config:
        env_file = "...env"

settings = Settings()
