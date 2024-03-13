SECRET_KEY = "yoursecretkey"
ALGORITHM = "HS256"

USERS = {
    "superuser": {
        "username": "superuser",
        "password": "supersafepassword",
        "is_superuser": True,
        "Company ID": None
    },
    "user1": {
        "username": "user1",
        "password": "password1",
        "is_superuser": False,
        "Company ID": 525
    },
    "user2": {
        "username": "user2",
        "password": "password2",
        "is_superuser": False,
        "Company ID": 520
    },
}