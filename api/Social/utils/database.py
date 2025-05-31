from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from api.Social.utils.config import settings

connection_url = URL.create(drivername="mysql+pymysql", username=settings.database_username, 
                            host=settings.database_hostname, 
                            password=settings.database_password, 
                            database=settings.database_name, 
                            port=settings.database_port)
Base = declarative_base()
engine = create_engine(connection_url)
sessionLocals = sessionmaker(autoflush=False, bind=engine)



