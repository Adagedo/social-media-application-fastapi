from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String 
from api.Social.models.abstractbase import AbstractBaseModel

class HashTag(AbstractBaseModel):
    __tablename__ = "hashtag"
    
    tag: Mapped[str] = mapped_column(String(55), nullable=False, unique=True)
    usage: Mapped[int] = mapped_column(Integer, default=1)

    def __str__(self):
        return self.tag