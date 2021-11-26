# Docker Compose + Local

# Inicio

Rodar

```
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```


inicializar os servico
```
docker-compose up airflow-init
```

rodar

```
docker-compose up
```
