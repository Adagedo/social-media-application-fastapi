from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import DateTime, ForeignKey, String, func
from api.Social.models.abstractbase import AbstractBaseModel


class CoverPhoto(AbstractBaseModel):
    
    __table__ = "cover_photo"
    
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"), nullable=False)
    image: Mapped[str] = mapped_column(String(1024), nullable=False)
    user = relationship("User", back_populates="cover_photos")
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __str__(self) -> str:
        return self.image