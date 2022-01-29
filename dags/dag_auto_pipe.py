import os
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from utils.util_sql_server import CORESQL
from utils.config import querys_auditoria
from utils.util_datalake import Datalake
import pandas as pd
from textwrap import dedent
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup
import sys

default_args = {
    'start_date': datetime(2021, 12, 6, 0, 0, 0),
    'depends_on_past': False,
}


def athena_ddl_create(file):
    print(file)

da = DAG(
    dag_id='teste_dag_auto_group',
    default_args=default_args,
    schedule_interval=None, 
    catchup=False,
    tags=['AUTOPIPE']
)

with da as dag:
    t0 = DummyOperator(task_id='start')
    t99 = DummyOperator(task_id='end')
    object_dict_dw_extractor = {
                'core':['fundos_pos',
                        'fundos_mov',
                        'renda_fixa_op',
                ],
                'core1':[
                        'renda_fixa_pos',
                        'fundos_bol',
                ],
                'core2':[
                        'cco_clientes',
                        'cco_teds',
                        'tb_operations',
                ],
                'sinacor':[],
                'salesforce':[],
    }
    lista_tarefas = []
    for g_id, value in object_dict_dw_extractor.items():
        list_group_exec = []
        with TaskGroup(group_id=f'group_work_{g_id}') as tg2:
            st0 = DummyOperator(task_id=f'start_{g_id}')
            st99 = DummyOperator(task_id=f'end_{g_id}')
            if len(value) > 0:
                for task in value:
                    with TaskGroup(group_id=f'group_exec_{g_id}_{task}') as tg1:
                        st1 = DummyOperator(task_id=f'task1_{task}')
                        st2 = PythonOperator(
                                    task_id=f'node_athena_{task}',
                                    python_callable=athena_ddl_create,
                                    op_kwargs={'file': 'renda_fixa_op'},
                        )
                        st3 = DummyOperator(task_id=f'task3_{task}')
                    
                    st1 >> st2 >> st3
                    list_group_exec.append(tg1)
                
        for exec_task in list_group_exec:
            st0 >> exec_task >> st99

        lista_tarefas.append([tg2])

for lista_group in lista_tarefas:
    t0 >> lista_group >> t99


# with da as dag:
#     t0 = DummyOperator(task_id='start')
#     t99 = DummyOperator(task_id='end')

#     lista_tarefas = []
#     for g_id, value in enumerate([1,2,3]):
#         with TaskGroup(group_id=f'group_work_{g_id}') as tg2:
#             st0 = DummyOperator(task_id='start')
#             st99 = DummyOperator(task_id='end')
#             with TaskGroup(group_id=f'group_exec_{g_id}') as tg1:
 
#                 st1 = DummyOperator(task_id='task1')
#                 st2 = DummyOperator(task_id='task2')
#                 st3 = DummyOperator(task_id='task3')
#             st1 >> st2 >> st3

#             st0 >> tg1 >> st99

#         lista_tarefas.append(tg2)

#     t0 >> lista_tarefas >> t99
