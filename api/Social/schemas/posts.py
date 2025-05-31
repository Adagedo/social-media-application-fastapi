from pydantic import ConfigDict, BaseModel, UUID4, Field
from api.Social.schemas.user import UserResponse
from datetime import datetime
from typing import Optional

class CreatePostSchema(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    content: str | None = None
    image: str | None = None
    video: str | None = None
    
    
class UpdatePostSchema(CreatePostSchema):
    pass


class PostResponse(CreatePostSchema):
    id:UUID4
    user_id: UUID4 = Field(exclude=True)
    created_at:datetime 
    updated_at: datetime
    user: UserResponse | None = Field(default=None, serialization_alias =  "original_post_owner")
    
    
class PostResponseSchemas(PostResponse):
    
    original_post: PostResponse | None = Field(default=None, serialization_alias="original_post")
  
    
class LikedResponse(BaseModel):
    
    model_config = ConfigDict(from_attribute=True)
    id: str
    post_id: str
    user_id: str
    liked: bool
    user: UserResponse = None


class RePostCreate(BaseModel):
    content:str |None = None
    

class RepostResponse(RePostCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str
    post_id: str = Field(exclude=True)
    user_id: str = Field(exclude=True)
    created_at: datetime
    updated_at: datetime
    user: UserResponse = Field(default=None, serialization_alias="post_owner")
    post: PostResponse = Field(default=None, serialization_alias="original_post")
    
