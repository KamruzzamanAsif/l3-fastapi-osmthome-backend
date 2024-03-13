from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from src.auth import constants, exceptions
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def create_jwt_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, constants.SECRET_KEY, algorithm=constants.ALGORITHM)

def get_user_by_username(username: str):
    if username in constants.USERS:
        user_dict = constants.USERS[username]
        return user_dict

async def get_current_user(token: str = Depends(oauth2_scheme)):
    
    try:
        payload = jwt.decode(token, constants.SECRET_KEY, algorithms=[constants.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise exceptions.credentials_exception
    except JWTError:
        raise exceptions.credentials_exception

    user = get_user_by_username(username)
    if user is None:
        raise exceptions.credentials_exception
    
    # print(username)


    return user