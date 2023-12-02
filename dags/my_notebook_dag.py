from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from common_modules.my_project import my_project
from datetime import datetime

# DAG constants
INITIAL_DATASET = "/tmp/outputs/my_notebook_dag/{{ logical_date }}/dataset.csv"
PROCESSED_DATASET = "/tmp/outputs/my_notebook_dag/{{ logical_date }}/processed_dataset.csv"

def print_hello():
    return "Hello world!"

with DAG(
    dag_id="my_notebook_dag", 
    description="DAG which shows how to use Papermill", 
    schedule_interval=None,
    start_date=datetime(2023, 1, 1), 
    catchup=False,
    tags=["uva"],
) as dag:
    hello_task = PythonOperator(task_id="hello_task", python_callable=print_hello)

    my_project_task = PythonOperator(
        task_id="my_project_task",
        python_callable=my_project.create_dataset,
        op_kwargs={"path": INITIAL_DATASET}
    )

    my_notebook_task = PapermillOperator(
        task_id="run_notebook",
        input_nb="/opt/airflow/dags/common_modules/notebooks/my_notebook.ipynb",
        output_nb="/tmp/outputs/my_notebook_dag/{{ logical_date }}/my_notebook-output.ipynb",
        parameters={
            "src_dataset": INITIAL_DATASET,
            "dst_dataset": PROCESSED_DATASET,
        }
    )

    hello_task >> my_project_task >> my_notebook_task
