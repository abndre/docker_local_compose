
Executar docker compose com serviços do airflow

docker-compose up airflow-init

docker-compose up postgres redis airflow-webserver airflow-scheduler airflow-cli flower airflow-triggerer

Executar airflow-worker localmente

instale o airflow 

pip install -r requirements.txt

export AIRFLOW_HOME=~/airflow

airflow celery worker
