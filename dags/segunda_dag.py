from datetime import timedelta
from textwrap import dedent
from pprint import pprint

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.operators.python import PythonOperator

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
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
    'segunda_dag',
    default_args=default_args,
    description='segunda_dag',
    schedule_interval="*/5 * * * *",#timedelta(days=1),
    start_date=days_ago(1),
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

    t1 >> run_this
