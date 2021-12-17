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
yarn start
```
The UI will be accessible at `http://localhost:3000/`

## Changing an app's name
The project is created with default apps `api`, `ui` and `batch_process` in the `apps` folder. You may want to change an app's name, for example `batch-process` to another name such as `batch_etl`, `batch_inference`. To do that, after renaming the app folder, you need to update related CICD/Helm chart files. As an example, here are the steps to change `batch_process` to `batch_etl`:
1. Rename `batch_process` to `batch_etl`.
2. Update the following files, replace `batch_process` by `batch_etl` and `batch-process` by `batch-etl`:
  - `.lighthouse/jenkins-x/python/pullrequest.yaml`
  - `.lighthouse/jenkins-x/python/release_batch.yaml`
  - `.lighthouse/jenkins-x/release.yaml`
  - `apps/batch_etl/Dockerfile`
  - `apps/batch_etl/pyproject.toml`
3. Rename `charts/{{cookiecutter.project_dir}}-batch-process` to `charts/{{cookiecutter.project_dir}}-batch-etl`.

4. Update the following files, replace `batch_process` by `batch_etl` and `batch-process` by `batch-etl`:
  - `charts/{{cookiecutter.project_dir}}-batch-etl/Chart.yaml`
  - `charts/{{cookiecutter.project_dir}}-batch-etl/Makefile.yaml`
  - `charts/{{cookiecutter.project_dir}}-batch-etl/README.md` (Optional)
3. Commit the code and push to github

## Adding new apps
To add a new app, you can copy an existing app, copy the corresponding Helm chart folder and update related CICD/Hem chart files. As an example, here are the steps to add one more batch process app for model inference:
1. Copy `apps/batch_process` folder into `apps/batch_inference` and update the following files, replace `batch_process` by `batch_inference` and `batch-process` by `batch-inference`:
  - `apps/batch_inference/Dockerfile`
  - `apps/batch_inference/pyproject.toml`

2. Copy `.lighthouse/jenkins-x/python/release_batch.yaml` into `.lighthouse/jenkins-x/python/release_batch_inference.yaml` and replace `batch_process` by `batch_inference` and `batch-process` by `batch-inference`.

3. Update `.lighthouse/jenkins-x/python/pullrequest.yaml`, add those lines to the end of the `script` section:
```python
cd apps/batch_inference
poetry check
poetry install --no-interaction
poetry run pylint --init-hook="sys.path.append('.')" **/*.py
poetry run pytest
```
3. Update the `.lighthouse/jenkins-x/release.yaml`:
  - Add the following lines to `spec.pipelineSpec.tasks` section:
  ```yaml
  - name: python-batch-inference-app-build
    taskSpec:
      steps:
        - image: uses:.lighthouse/jenkins-x/python/release_batch_inference.yaml
  ```
  - Add the following line to `spec.pipelineSpec.tasks.name` section:
  ```yaml
  - python-batch-inference-app-build
  ```
  - Add the following line to the `script` section of the `promote-jx-promote` step
  ```shell
  jx promote --app {{cookiecutter.project_dir}}-batch-inference --version $VERSION -b --all --timeout 1h
  ```

4. Copy `charts/{{cookiecutter.project_dir}}-batch-process` folder into `charts/{{cookiecutter.project_dir}}-batch-inference`.
5. Update the following files, replace `batch_process` by `batch-inference` and `batch-inference` by `batch-etl`:
  - `charts/{{cookiecutter.project_dir}}-batch-inference/Chart.yaml`
  - `charts/{{cookiecutter.project_dir}}-batch-inference/Makefile.yaml`
  - `charts/{{cookiecutter.project_dir}}-batch-inference/README.md` (Optional)
6. Commit the code and push to github




