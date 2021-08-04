# {{cookiecutter.project_name}}
## Running the application

### Prerequisites
1. Python 3.8.10
2. [Poetry](https://python-poetry.org/docs/#installation) 
3. Nodejs 16.2.0

### Starting the server
```shell
poetry install
poetry run python manage.py runserver
```
The server will be running and a request to `http://localhost:8000/api/foo` will respond with 200 OK.

### Starting the UI
```shell
nvm use v16.2.0
cd h1st_react
yarn start
```
The UI will be accessible at `http://localhost:3000/`