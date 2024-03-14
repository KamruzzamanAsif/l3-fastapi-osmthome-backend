from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.auth import exceptions, service

router = APIRouter()


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    This endpoint accepts a POST request to authenticate a user with their username and password.
    The `form_data` parameter is an instance of the `OAuth2PasswordRequestForm` class, which defines the schema for the request body.
    It must contain a `username` and `password` field.
    The `service.get_user_by_username()` function is called to retrieve the user with the given username.
    If the user is not found or the password is incorrect, a `credentials_exception` is raised.
    Otherwise, a JWT token is created with the user's username as the subject and returned in the HTTP response body.
    """
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
    """
    This endpoint accepts a GET request to retrieve information about the authenticated user.
    The `current_user` parameter is an instance of the `dict` class, which will be populated by the `service.get_current_user()` dependency.
    If the user is not authenticated, a `HTTPException` with a status code of 401 (Unauthorized) will be raised.
    Otherwise, the user data is returned in the HTTP response body.
    """
    return current_user


@router.get("/user1")
async def only_user1_can_access_this(
    current_user: dict = Depends(service.get_current_user),
):
    """
    This endpoint accepts a GET request to retrieve information about user 1.
    The `current_user` parameter is an instance of the `dict` class, which will be populated by the `service.get_current_user()` dependency.
    If the user is not authenticated, a `HTTPException` with a status code of 401 (Unauthorized) will be raised.
    If the user's `Company ID` is not 525, a `credentials_exception` is raised.
    Otherwise, the user data is returned in the HTTP response body.
    """
    if current_user["Company ID"] != 525:
        raise exceptions.credentials_exception

    return current_user


@router.get("/user2")
async def only_user2_can_access_this(
    current_user: dict = Depends(service.get_current_user),
):
    """
    This endpoint accepts a GET request to retrieve information about user 2.
    The `current_user` parameter is an instance of the `dict` class, which will be populated by the `service.get_current_user()` dependency.
    If the user is not authenticated, a `HTTPException` with a status code of 401 (Unauthorized) will be raised.
    If the user's `Company ID` is not 520, a `credentials_exception` is raised.
    Otherwise, the user data is returned in the HTTP response body.
    """
    if current_user["Company ID"] != 520:
        raise exceptions.credentials_exception

    return current_user
