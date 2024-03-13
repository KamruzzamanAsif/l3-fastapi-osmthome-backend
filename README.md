# l3-fastapi-osmthome-backend


# Project setup
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


# Project Documentation
## 1. Structure
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

## 2. Structure Overview
* l3-fastapi-osmthome-backend is the root directory
* src contains all the independent modules and global .py files
* test directory contains all the test cases for each independent module
* .env contains all the environment variables
* .env.example is the skeleton of the .env file
* .venv is the virtualenv of the project
* .pre-commit-config.yaml file contains all the pre-commit configurations(with linters)
* poetry.lock contains all the the necessary python package information (this is auto generated)
* pyproject.toml contains project setup information & tool configurations
* .gitignore contains the names of the files & directories that are ignored fom git tree
* README.md contains the project documentation

## 3. How to install a python package?
To install a python package to the project just follow the command below <br/>
``` poetry add package-name ``` <br/>
eg. `poetry add fastapi`
This will install the python package and automatically update the *pyproject.toml* file.

## 4. How to run the project?
To run the project use this command in your shell/terminal from the root dirctroy <br/>
``` poetry run app ```

## 5. Src Directory Documentation
src quick view
```
src
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
│   └── template-module
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
```
> src/main.py
* this is the main file whre the fastapi application initalizes
> src/config.py
* this file should contain all the global configurations(like db configs, and other configurations)
> src/models.py
* this file should contain all the the global models that are common to all the independent modules
> src/exceptions.py
* this file should contain all the the global exceptions that are common to all the independent modules
> src/database.py
* this file should contain all the the db connection related stuff that are common to all the independent modules

### Module Overview
* Each Module is Independent
* You can add your own modules and implement your own
* Please follow the template-module structure from the project documentation but it is not strictly necessary to follow the same structure
* After implementing your own module you must make sure your modules router endpoints are added in src/main.py file otherwise it will not be accessible <br/>
(To get a quick look how the route end point is added from my vessel module you can see the src/main.py file and src/vessel/route.py file)

### Authentication module (Not implemented yet)
Authentication module should contain all the authentication related stuffs

### Vessel module
Vessel module contains 3 files:
* config.py file: this file contains all the db config related stuff (variables)
* database.py file: this file contains all the db connection method and return a db connection object
* service.py file: this file contains business logic related stuff. This holds methods for querying db tables, fetching data and adding business logic to them to provide required output
* router.py file: this file contains the router endpoints (for now there is one named '/vessel/' which return total number of vessels)
