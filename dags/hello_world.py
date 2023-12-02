from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    return "Hello world!"

with DAG(
    dag_id="hello_world_dag", 
    description="First DAG", 
    schedule_interval="*/10 * * * *", 
    start_date=datetime(2023, 1, 1), 
    catchup=False,
    tags=["uva"],
) as dag:
    hello_task = PythonOperator(task_id="hello_task", python_callable=print_hello)

    hello_task
