from typing import List, Optional
from datetime import datetime
from enum import Enum
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    String,
    Table,
    func,
    Enum as SQLAlchemyEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api.Social.models.abstractbase import AbstractBaseModel
from api.Social.utils.database import Base


class RoleEnum(Enum):
    user = "user"
    admin = "admin"


followers_table = Table(
    "user_interaction",
    Base.metadata,
    Column("follower_id", String, ForeignKey("user.id"), primary_key=True),
    Column("followed_id", String, ForeignKey("user.id"), primary_key=True),
)


class User (AbstractBaseModel):
    
    __tablename__ = "user"
    