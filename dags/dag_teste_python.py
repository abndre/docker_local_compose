"""
### ETL DAG Tutorial Documentation
This ETL DAG is compatible with Airflow 1.10.x (specifically tested with 1.10.12) and is referenced
as part of the documentation that goes along with the Airflow Functional DAG tutorial located
[here](https://airflow.apache.org/tutorial_decorated_flows.html)
"""

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

}


def fazer_alguma_coisa(p1, **kwargs):
    pprint(kwargs)
    print(p1)
    return 'Whatever you return gets printed in the logs'

def fazer_outra_coisa(p1, **kwargs):
    pprint(kwargs)
    print(p1)
    return 'FIM'



with DAG(
    'dag_para_clicar_nasegunda',
    default_args=default_args,
    description='dag_para clicar_nasegunda',
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['python'],
    catchup=False
) as dag:
    # [START documentation]
    dag.doc_md = __doc__
    # [END documentation]
    run_this = PythonOperator(
        task_id='print_the_context',
        provide_context=True,
        python_callable=fazer_alguma_coisa,
        op_kwargs={'p1': 'parametro passado', 't2':'Outro parametro'})

    or_this = PythonOperator(
        task_id='print_the_other_context',
        provide_context=True,
        python_callable=fazer_alguma_coisa,
        op_kwargs={'p1': 'foi a segunda', 't2':'Outro parametro'})

run_this >> or_this
