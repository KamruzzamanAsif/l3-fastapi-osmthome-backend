# Project Documentation

## Structure
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
|   ├── hseq
│   │   ├── api     # all api endpoints for this module
│   │   │ ├── cdi_router.py
│   │   │ ├── health_safety_router.py
│   │   │ ├── psc_router.py
│   │   │ └── sire_router.py
│   │   ├── service     # business logics & relevant methods
│   │   │ ├── cdi_service.py
│   │   │ ├── health_safety_service.py
│   │   │ ├── psc_service.py
│   │   │ └── sire_service.py
│   │   ├── database    # database connection for relevant section
│   │   │ ├── cdi_database.py
│   │   │ ├── health_safety_database.py
│   │   │ ├── psc_database.py
│   │   │ └── sire_database.py
│   │   ├── models  # should contain EDMs (entity data models)
│   │   │ ├── cdi_observations.py
│   │   │ ├── critical_overdue_jobs.py
│   │   │ ├── sire_observations.py
│   │   │ ├── vessel_count.py
│   │   │ └── watch_list.py
│   │   ├── config.py   # all configs in this module
│   │   ├── exceptions.py   # all exceptions in this module
|   ├── XYZ_MODULE
│   │   ├── api     # all api endpoints for this module
│   │   │ ├── a_router.py
│   │   │ ├── b_router.py
│   │   ├── service     # business logics & relevant methods
│   │   │ ├── a_service.py
│   │   │ ├── b_safety_service.pyy
│   │   ├── database    # database connection for relevant section
│   │   │ ├── a_database.py
│   │   │ ├── b_database.py
│   │   ├── models  # should contain EDMs (entity data models)
│   │   │ ├── a_model.py
│   │   │ ├── b_model.py
│   │   ├── config.py   # all configs in this module
│   │   ├── exceptions.py   # all exceptions in this module
│   ├── config.py   # global configs for entire project
│   ├── models.py   # global models for entire project
│   ├── exceptions.py   # global exceptions for entire project
│   ├── database.py     # global db connection related stuff for entire project
│   └── main.py
├── tests
│   ├── auth
│   ├── hseq
├── .env
├── .venv
├── .pre-commit-config.yaml
├── poetry.lock
├── pyproject.toml
├── .gitignore
├── README.md
```

### Structure Overview
* l3-fastapi-osmthome-backend is the root directory
* src contains all the independent modules and global python files
* test directory contains all the test cases for each independent module
* .env contains all the environment variables
* .env.example is the skeleton of the .env file
* .venv is the virtualenv of the project
* .pre-commit-config.yaml file contains all the pre-commit configurations(with linters)
* poetry.lock contains all the the necessary python package information (this is auto generated)
* pyproject.toml contains project setup information & tool configurations
* .gitignore contains the names of the files & directories that are ignored fom git tree
* README.md contains the project documentation

#### Src Directory Overview
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
> src/auth
* this is authentication module which contains authentication related stuff (see Structure for more information)
> src/hseq
* this is hseq module which contains hseq related stuff (see Structure for more information)



## Project setup
This project is setup with Python Packaging and Dependency Manager [Poetry](https://python-poetry.org/)
<br/>

### Step 1: Install Poetry
To install Poetry see this official [documentation](https://python-poetry.org/docs/#installation) <br>

```pipx install poetry```

### Step 2: Virtual Environment Configurations (Optional)
If you like to use in porject virtual environment then you can set up like this: <br>
```poetry config virtualenvs.in-project true```

### Step 3: Install Project Dependencies
```poetry install```

### Step 4: Setup Precommit with git (For linters and Commit configs)
```pre-commit install```

### Step 5: Configure your .env file
* Create a .env file at the root directory. Copy and paste the configuration fields from .env.example
* Fill up the configuration fields with your own credentials

### Step 5: Run the Application
```poetry run app```


## How to install a python package?
To install a python package to the project just follow the command below <br/>
``` poetry add package-name ``` <br/>
eg. `poetry add fastapi`
This will install the python package and automatically update the *pyproject.toml* file.

## How to run the project?
To run the project use this command in your shell/terminal from the root dirctroy <br/>
``` poetry run app ```


## About Git Commit
1. when you add and commit git changes the linters in the pre-commit will check and find errors.
2. if any errors are found the linters will automatically fix those but the commit will not done.
3. you have to again add and commit the changes for a successful commit.
4. then you can push the changes to github repository



jhj
