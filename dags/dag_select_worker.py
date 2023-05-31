from airflow.decorators import task
from airflow import DAG
from time import sleep
from datetime import datetime
with DAG(
        "dag_select_worker",
        start_date=datetime(2023, 5, 29),
        schedule_interval=None,
        catchup=False,
        max_active_runs=5
) as dag:
    @task(queue='dados')
    def get_name(timer=60):
        print(f"TASK: {timer}")
        sleep(60)

    task1 = get_name()

    task2 = get_name(40)

task1 >> task2