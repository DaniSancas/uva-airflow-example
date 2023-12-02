from airflow import DAG
from airflow.operators.python import PythonOperator
from common_modules.my_project import my_project
from datetime import datetime

def print_hello():
    return "Hello world!"

with DAG(
    dag_id="my_project_dag", 
    description="DAG which executes my_project", 
    schedule_interval=None,
    start_date=datetime(2023, 1, 1), 
    catchup=False,
    tags=["uva"],
) as dag:
    hello_task = PythonOperator(task_id="hello_task", python_callable=print_hello)

    my_project_task = PythonOperator(
        task_id="my_project_task",
        python_callable=my_project.create_dataset,
        op_kwargs={"path": "/tmp/outputs/my_project_dag/dataset.csv"}
    )

    hello_task >> my_project_task
