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
