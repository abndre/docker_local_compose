"""
###  DAG DOCE
Alguem texto de importancia
"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
# from airflow.operators.docker_operator import DockerOperator
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    'owner'                 : 'airflow',
    'description'           : 'documentacao',
    'depend_on_past'        : False,
    'start_date'            : datetime(2018, 1, 3),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}



dag = DAG(
    dag_id='documentacao_funcionando',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    dagrun_timeout=timedelta(minutes=60),
    catchup=False,
    tags=['doc']
)

# [START documentation]
dag.doc_md = __doc__
# [END documentation]

# Imprime a data na saída padrão.
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

t1