# Challenge N5
This Challenge is about manage a infractions app. Interface and API will requirements.

## Python Version
`>3.8`


## Install this if you need to development
> or if you wanna run the project with virtualenv and the command uvicorn from server

## Install Base dependency
`pip install -r requirements/base.txt`

### How to set up dev tools
* install dev requirements  `pip install -r requirements/dev.txt`
* run  `pre-commit install`

### How to set up linters tools
* install linters requirements  `pip install -r requirements/linters.txt`

### How to run linters?
There are 3 types of linters:
* Black: Which formats the python code to black style: `black apps/`
* Flake8: which analyze code: `flake8 apps/`
* Isort: isort your imports, so you don't have to: `isort apps/ --profile black`

```
Check Yaml...............................................................Passed
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
black....................................................................Passed
flake8...................................................................Passed
isort....................................................................Passed
```

### You can also run all linters as follows:

* `pre-commit run --all-files`
