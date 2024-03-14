from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from src.auth import constants, exceptions

# Create an instance of OAuth2PasswordBearer, which is a class provided by FastAPI for handling OAuth2 password-based authentication.
# The `tokenUrl` argument specifies the URL that will be used for the token, which is "/token".
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def create_jwt_token(data: dict):
    """
    This function takes a dictionary containing data that will be encoded into a JWT token.
    The `to_encode` dictionary is created as a copy of the input dictionary, so as not to modify the original.
    The `jwt.encode()` function is then called to create the token, using the `constants.SECRET_KEY` and `constants.ALGORITHM` values.
    """
    to_encode = data.copy()
    return jwt.encode(to_encode, constants.SECRET_KEY, algorithm=constants.ALGORITHM)


def get_user_by_username(username: str):
    """
    This function takes a username string and returns the corresponding user dictionary from the `constants.USERS` dictionary.
    If the username is not found in the dictionary, `None` is returned.
    """
    if username in constants.USERS:
        user_dict = constants.USERS[username]
        return user_dict


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    This asynchronous function is a FastAPI dependency, which is a way to automatically pass data between endpoints.
    In this case, it is used to retrieve the current user's data from a JWT token.
    The function first decodes the token using the `jwt.decode()` function, passing in the `constants.SECRET_KEY` and `constants.ALGORITHM` values.
    If the token cannot be decoded or the `sub` (subject) field is missing, a `credentials_exception` is raised.
    Otherwise, the `sub` field is retrieved and used to look up the corresponding user dictionary.
    If the user is not found, a `credentials_exception` is raised.
    """
    try:
        payload = jwt.decode(
            token, constants.SECRET_KEY, algorithms=[constants.ALGORITHM]
        )
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
