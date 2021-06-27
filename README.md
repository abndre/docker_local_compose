#Projeto Airflow Docker-Compose + Docker-Operator

Para rodar dags com melhor CI/CD utilizo o dockeroperator. E como o projeto ja roda em docker,
nao seria muito bom rodar um container dentro de um container.

Assim, o worker roda fora dos containers. De modo ao mesmo ser, uma instancia de maior
poder de processamento

## Executando

´´´
docker-compose up airflow-init

docker-compose up postgres redis airflow-webserver airflow-scheduler flower

airflow celery worker  

´´´
