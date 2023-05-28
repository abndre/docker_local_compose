from datetime import timedelta, datetime
from textwrap import dedent
from pprint import pprint

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.operators.python import PythonOperator

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from airflow.decorators import dag, task

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2022, 5, 27),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}


def fazer_alguma_coisa(p1, **kwargs):
    pprint(kwargs)
    print(p1)
    return 'Whatever you return gets printed in the logs'

with DAG(
    'dag_create_folder_and_file',
    default_args=default_args,
    description='segunda_dag',
    schedule_interval=None,
    tags=['example'],
    catchup=False
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    run_this = PythonOperator(
        task_id='print_the_context',
        provide_context=True,
        python_callable=fazer_alguma_coisa,
        op_kwargs={'p1': 'parametro passado', 't2':'Outro parametro'})

    
    @task
    def hello_task_decorator():
        import pandas as pd
        import os
        print("Hello Task decorator")
        # initialize list elements
        data = [10,20,30,40,50,60]
  
        # Create the pandas DataFrame with column name is provided explicitly
        df = pd.DataFrame(data, columns=['Numbers'])
        path = f"{os.getenv('AIRFLOW_HOME')}/data_dag/teste.csv"
        print(path)
        df.to_csv(path, index=False)

    task_hello_task_decorator = hello_task_decorator()


t1 >> run_this >> task_hello_task_decorator
