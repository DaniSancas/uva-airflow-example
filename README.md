# UVa Airflow example

## How to install Airflow

### Pre-requisites

- Python >=3.10
- Docker

### Project initialization

- Clone this repo.
- Open a terminal inside the repo and execute the following instructions:

```bash
# Set an expected environment variable
echo -e "AIRFLOW_UID=$(id -u)" > .env

# Build the image
docker-compose build

# Initialize the database
docker-compose up airflow-init

# Start up all services
docker-compose up
```
Note: These instructions are very similar to the [official tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/pipeline.html#initial-setup)

This should start the **Airflow Server**. Then:
- Navigate to http://0.0.0.0:8080/
- Login with user/pass: `airflow` / `airflow`
- The UVa DAGs are tagged with `uva`. You can filter them: http://0.0.0.0:8080/home?tags=uva

## How to install projects dependencies

Needed to execute the DAGs that uses the Python code in `common_modules` and to test the notebooks.

```bash
pipenv --python 3.10
pipenv install
```

## hello_world DAG

This example is very simple, just go to [hello_world DAG](http://0.0.0.0:8080/dags/hello_world/grid) and execute it.

## my_project: module and DAG

We can execute `my_project` module without the DAG first.

```bash
pipenv run python dags/common_modules/my_project/my_project.py
```

It should output `Dataset stored at: /tmp/uva/dataset.csv`

To execute via DAGs, we head to [my_project_dag DAG](http://0.0.0.0:8080/dags/my_project_dag/grid) and execute it. The output should appear in `outputs/my_project_dag/dataset.csv`

## my_notebook: notebook and DAG

We can test `my_notebook.ipynb` notebook without the DAG first.

```bash
pipenv run jupyter-notebook
```

Then, open the Jupyter UI and navigate to [/notebooks/dags/common_modules/notebooks/my_notebook.ipynb](http://127.0.0.1:8888/notebooks/dags/common_modules/notebooks/my_notebook.ipynb)

You should be able to execute all the cells successfully.

To execute via DAGs, we head to [my_notebook_dag DAG](http://0.0.0.0:8080/dags/my_notebook_dag/grid) and execute it. The outputs should appear in `outputs/my_notebook_dag/<execution_date>/`, where `<execution_date>` is the timestamp when the DAG was executed (example: 2023-12-02T16:31:20.888124+00:00)

There you should see:
- `dataset.csv`
- `processed_dataset.csv`
- `my_notebook-output.ipynb`
