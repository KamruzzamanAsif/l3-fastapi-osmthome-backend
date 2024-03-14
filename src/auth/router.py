from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from src.auth import service, exceptions


router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    user = service.get_user_by_username(username)
    if user is None or user["password"] != password:
        raise exceptions.credentials_exception

    token_data = {"sub": username}
    token = service.create_jwt_token(token_data)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/users/me", response_model=dict)
async def who_am_i(current_user: dict = Depends(service.get_current_user)):
    return current_user

@router.get("/user1")
async def only_user1_can_access_this(current_user: dict = Depends(service.get_current_user)):
    if current_user['Company ID'] != 525:
        raise exceptions.credentials_exception
    
    return current_user

@router.get("/user2")
async def only_user2_can_access_this(current_user: dict = Depends(service.get_current_user)):
    if current_user['Company ID'] != 520:
        raise exceptions.credentials_exception
    
    return current_user