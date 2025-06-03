from fastapi import Depends, HTTPException, Response, status, BackgroundTasks
from api.Social.schemas.user import (
    User as UserSchema, 
    UserCreateResponse, 
    UserLoginSchema, 
    UserResponse, 
    UserUpdateSchema, 
    UserLoginS, 
    CreateUserSchema
)
from api.Social.models.profile_picture import ProfilePicture
import api.Social.models.notification as notification_model
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, text
from api.Social.services.auth.utils import hashedPassword, verify_password
import api.Social.models.user as user_model 
from api.Social.services.auth.authentication_service import UserAuthenticationService
from api.Social.utils.config import settings
from datetime import datetime, timedelta, timezone
from api.Social.models.cover_photo import CoverPhoto
from api.Social.models.social_links import SocialLink
from fastapi.encoders import jsonable_encoder
from api.Social.services.notification import notification_service

class UserService(UserAuthenticationService):

    
    def create_user(self, user:CreateUserSchema, db:Session):
        try:
            
            if self.exists(user.email, db):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with email already exists")
            
            hashedPassword = hashedPassword(user.password)
            user.password = hashedPassword
            user = user_model.User(**user.model_dump())
            
            db.add(user)
            db.commit()
            db.refresh(user)
            
            notification = notification_model.Notification(
                user_id=user.id, message="Account created successfully"
            )
            
            db.add(notification)
            db.commit()
            
            token_data = {
                "user":user.username,
                "role": user.role,
                "id": user.id
            }
        except Exception as e: raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
        
    
    def exists(self, email:str, db:Session) -> bool:
        try:
            
            user = db.query(user_model.User).filter(user_model.User.email == email).first()
            if not user:
                return False
            
            return True
        except Exception as e: raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
    
    def get_user_by_email(self, email:str, db:Session) -> user_model.User | None:
        
        try:
            user = db.query(user_model.User).filter(user_model.User.email == email).first()
            if not user:
                raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND, detail=f"user with the email does not exist"
                )
        
        except Exception as e: raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"server error {e}"
        )
        
        return user
    
    def handel_user_login(self, userLogin:UserLoginS, db:Session, response:Response):
        
        user = db.query(user_model.User).filter(user_model.User.email == userLogin.email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials"
            )
        
        is_valid_password = verify_password(userLogin.password, user.password)
        
        if not is_valid_password:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, detail="invalid credentials"
            )
            
        token_payload = {
            "email":user.email,
            "username":user.username,
            "user_id":user.id,
            "role": user.role
        }
        access_token:str = self.generate_access_token(token_payload)
        response.set_cookie(
            key=settings.cookie_key, value=access_token, expires=settings.access_token_expires_minutes, 
            secure=True, httponly=True, samesite="strict"
        )
        
        user.last_login = datetime.now(timezone.utc)
        db.commit()
        db.refresh(user)
        
        notification = notification_model.Notification(
            user_id=user.id, message="Account login successful"
        )
        
        db.add(notification)
        db.commit()
        db.refresh(notification)
        
        client_user_response = jsonable_encoder(
            self.get_user_details(db=db, user_id = user.id), exclude={"password"}
        )
        
        response = {
            "user":client_user_response
        }
        
        return response
        
    
    def get_user_details(self, db:Session, user_id):
        query = (
            db.query(user_model.User)
            .options(
                joinedload(user_model.User.profile_pictures),
                joinedload(user_model.User.cover_photos),
                joinedload(user_model.User.followers),
                joinedload(user_model.User.social_links),
                joinedload(user_model.User.username),
                joinedload(user_model.User.bio),
                joinedload(user_model.User.followings),
                joinedload(user_model.User.posts),
                joinedload(user_model.User.email),
                joinedload(user_model.User.notifications)
            ).filter(user_model.User.id == user_id).first()
        )
        
        if not query:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, detail="user not found"
            )
        
        return query
        # generate notification
        
    
    def update_user_profile(self, user:user_model.User, schema:UserUpdateSchema, user_id:str, db:Session):
        
        if user.id != user_id:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN, detail="invalid action"
            )
        
        data = schema.model_dump(exclude_unset=True)
        
        profile_picture = data.pop("profile_picture", None)
        
        if profile_picture:
            
            #upload image to cloudinary
            # yet to implement thi method
            image_url = upload(profile_picture)
            
            #create a new profile picture 
            new_profile_picture = ProfilePicture(
                user_id=user.id, image=image_url
            )
            
            db.add(new_profile_picture)
            db.commit()
            db.refresh(new_profile_picture)
            
        cover_photo = data.pop("cover_photo", None)
        
        if cover_photo:
            
            #upload image to cloudinary
            image_url = upload(cover_photo)
            
            #create a new profile picture 
            new_cover_photo = CoverPhoto(
                user_id=user.id, image=image_url
            )
            
            db.add(new_cover_photo)
            db.commit()
            db.refresh(new_cover_photo)
        
        social_links = data.pop("social_link", [])
        if social_links:
            
            #removed all associated social links 
            db.query(SocialLink).filter(SocialLink.id == user.id).delete()
            db.flush()
            
            #create new links
            
            for link in social_links:
                social_link = SocialLink(link=link, user_id = user.id)
                
                db.add(social_link)
                
            db.commit()
        
        for key, value in data.items():
            
            setattr(user, key, value)
            
        db.commit()
        db.refresh(user)
        
        notification = notification_model.Notification(
            user_id = user.id , message="Account updated successfully"
        )
        
        db.add(notification)
        db.commit()
        
        return jsonable_encoder(
            self.get_user_detail(db=db, user_id=user_id, exclude={"password"})
        )
    
    def delete_user_profile(self, db:Session, user:user_model.User, user_id:str):
        
        if user.id != user_id:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN, 
                detail="invalid action"
            )
        
        db.delete(user)
        db.commit()
        
    
    def fetch_all(self, db:Session, search:str=""):

        query = (db.query(user_model.User).
                 options(
                    joinedload(user_model.User.profile_picture),
                    joinedload(user_model.User.social_links) 
                ).order_by(text("RANDOM()"))
            )
        
        if search:
            query = query.filter(
                or_(
                    user_model.User.username.icontains(f"%{search}%"),
                    user_model.icontain(f"%{search}%")
                )
            )
            
        users = query.all()
        
        return jsonable_encoder(users, exclude={"password"})
            
    
    def follow_user(self, db:Session, user_id:str, user:user_model.User, background_task:BackgroundTasks):
        
        followee = db.query(user_model.User).filter(user_model.User.id == user_id).first()
        
        if not followee:
            raise HTTPException(
                
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="user not found"
            )
        
        if followee not in user.followings:
            user.followings.append(followee)
            
            notification = notification_model.Notification(
                user_id = followee.id, message = f"{user.username} followed you"
            )
            db.add(notification)
            db.commit()

            background_task.add_task(notification_service.user_event_queues[notification.user_id].put, notification.message)
        
        
    def unfollow_user(self, db:Session, user_id:str, user:user_model.User, background_task:BackgroundTasks):
        
        user_to_unfollow = db.query(user_model.User).filter(user_model.User.id == user_id).first()
        
        if not user_to_unfollow:
            
            raise HTTPException(status_code=404, detail="User not found")
        
        if user_to_unfollow not in user.followings:
            raise HTTPException(
                status_code=404, detail="You are not following this user"
            )
        
        user.followings.remove(user_to_unfollow)
        
        notification = notification_model.Notification(
            user_id=user_to_unfollow.id, message=f"{user.username} unfollowed you"
        )
        
        db.add(notification)
        db.commit()
        
        background_task.add_task(notification_service.user_event_queues[notification.user_id].put, notification.message)
        
        
    def followers(self, db: Session, user: user_model.User):

        followers = [
            UserResponse(**jsonable_encoder(follower)) for follower in user.followers
        ]

        return followers
    
    
    def followings(self, db: Session, user: user_model.User):

        followings = [
            UserResponse(**jsonable_encoder(following)) for following in user.followings
        ]

        return followings


user_service = UserService()