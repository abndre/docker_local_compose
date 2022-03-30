from hello_operator import HelloOperator

from datetime import datetime
from airflow.models import DAG


default_args = {
    'start_date': datetime(2021, 12, 6, 0, 0, 0),
    'depends_on_past': False,
}


da = DAG(
    dag_id='dag_teste_custom_operator',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
)

with da:
    hello_task = HelloOperator(task_id="sample-task", name="foo_bar")


hello_task