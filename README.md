# l3-fastapi-osmthome-backend

# Project Structure
```
l3-fastapi-osmthome-backend
├── src
│   ├── auth
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   │   ├── dependencies.py
│   │   ├── config.py  # local configs
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py # business logics & core methods
│   │   └── utils.py # utility methods
|   └── vessel
│   │   ├── router.py
│   │   ├── config.py # local configs
│   │   ├── database.py # db connection
│   │   ├── service.py # business logics & core methods
│   └── template-package
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── config.py  # global configs
│   ├── models.py  # global models
│   ├── exceptions.py  # global exceptions
│   ├── database.py  # global db connection related stuff
│   └── main.py
├── tests/
│   ├── auth
│   ├── vessel
├── .env
├── .venv
├── .pre-commit-config.yaml
├── poetry.lock
├── pyproject.toml
├── .gitignore
├── README.md
```

## Project setup
This project is setup with Python Packaging and Dependency Manager [Poetry](https://python-poetry.org/)

<br/>

### Setp 1: Install Poetry
```pip install poetry```

### Setp 2: Poetry Configurations
```poetry config virtualenvs.in-project true```

### Setp 3: Install Project Dependencies
```poetry install```

### Setp 4: Setup Precommit with git
```precommit install```

### Setp 5: Configure your .env file
* Create a .env file at the root directory. Copy and paste the configuration fields from .env.example
* Fill up the configuration fields with your own credentials

### Setp 5: Run the Application
```poetry run app```
