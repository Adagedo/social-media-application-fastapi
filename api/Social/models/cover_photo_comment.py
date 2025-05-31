from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api.Social.models.abstractbase import AbstractBaseModel


class ProfilePhotoComment(AbstractBaseModel):
    __tablename__ = "profile_photo_comment"

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="comments")
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __str__(self) -> str:
        return self.comment