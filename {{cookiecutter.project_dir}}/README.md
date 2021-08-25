# {{cookiecutter.project_name}}

## Running the application using docker-compose
### Prerequisites
1. docker
2. docker-compose

### Starting the app
```shell
docker-compose build
docker-compose up -d
```
The app will be running and accessible at `http://localhost:80/`

### Stopping the app
```shell
docker-compose stop
```

## Running the application

### Prerequisites
1. Python 3.8.11
2. [Poetry](https://python-poetry.org/docs/#installation) 
3. Nodejs 16.2.0

### Starting the server
```shell
poetry install
poetry run python manage.py runserver
```
The server will be running and a request to `http://localhost:8000/api/v1/foo` will respond with 200 OK.

### Starting the UI
```shell
cd react_app
yarn install
export REACT_APP_SERVER_HOST=localhost 
export REACT_APP_SERVER_PORT=8000 
yarn start
```
The UI will be accessible at `http://localhost:3000/`