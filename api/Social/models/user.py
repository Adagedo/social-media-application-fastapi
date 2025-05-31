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
    
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(1024), nullable=False)
    bio: Mapped[Optional[str]] = mapped_column(String(1024))
    contact_info: Mapped[Optional[str]] = mapped_column(String(15))
    followings = relationship(
        "User",
        secondary=followers_table,
        primaryjoin=lambda: User.id == followers_table.c.followed_id,
        secondaryjoin=lambda: User.id == followers_table.c.follower_id,
        backref="followers",
    )
    role: Mapped[str] = mapped_column(SQLAlchemyEnum(RoleEnum), default=RoleEnum.user)
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )