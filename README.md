# UVa Airflow example

## How to install Airflow

### Pre-requisites

- Python >=3.10
- Docker

### Project initialization

- Clone this repo.
- Open a terminal inside the repo and execute the following (instructions from the [official tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/pipeline.html#initial-setup))

```bash
# Set an expected environment variable
echo -e "AIRFLOW_UID=$(id -u)" > .env

# Initialize the database
docker-compose up airflow-init

# Start up all services
docker-compose up
```

This should start the **Airflow Server**. Then:
- Navigate to http://0.0.0.0:8080/
- Login with user/pass: `airflow` / `airflow`
- The UVa DAGs are tagged with `uva`. You can filter them: http://0.0.0.0:8080/home?tags=uva

## How to install projects dependencies

Needed to execute the DAGs that uses the Python code in `common_modules`.

```bash
pipenv --python 3.10
pipenv install
```

## hello_world DAG

## my_project DAG

We can execute `my_project` module without the DAG first.

```bash
pipenv run python dags/common_modules/my_project/my_project.py
```

It should output `Dataset stored at: /tmp/uva/dataset.csv`

To execute via DAGs, we head to [my_project DAG](http://0.0.0.0:8080/dags/my_project_dag/grid) and execute it. The output should appear in `outputs/my_project_dag/dataset.csv`