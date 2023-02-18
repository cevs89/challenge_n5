# Challenge N5
This Challenge is about manage a infractions app. Interface and API will requirements.

## Python Version
`>3.8`

## Run server

***
## Virtual Enviroment
> You has to have installed  `virtualenv` and `pip`

**1.- Initial your virtualenv**
`virtualenv <path> --python=python3.8`

**2.- Active your virtualenv**
`source <path>/bin/activate`

**3.- Install Dependency**
`pip install -r requirements/base.txt`

**4.- Run local server**
`python manage.py runserver`
***
### Docker

***
## Install this if you need to development
> Before you has to install Virtual Enviroment

### 1.- How to set up dev tools
* install dev requirements  `pip install -r requirements/dev.txt`
* run  `pre-commit install`

### 2.- How to set up linters tools
* install linters requirements  `pip install -r requirements/linters.txt`

### 3.- How to run linters?
There are 3 types of linters:
* Black: Which formats the python code to black style: `black apps/`
* Flake8: which analyze code: `flake8 apps/`
* Isort: isort your imports, so you don't have to: `isort apps/ --profile black`

### 4.- You can also run all linters as follows:

* `pre-commit run --all-files`

Details before run
```
Check Yaml...............................................................Passed
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
black....................................................................Passed
flake8...................................................................Passed
isort....................................................................Passed
```
