# Projeto Docker Compose Prod

Como utilizar um projeto de docker compose para utilizar o apache-airflow em produção.

# Iniciando

Faça o build da imagem docker

```sh
docker compose build
```

Crie as pastas

```sh
mkdir -p ./dags ./logs ./plugins ./config
```

## Inicio o Projeto

Se for a primeira vez ao iniciar o projeto
```sh
docker compose up airflow-init
```
Agora inicie os serviços
```sh
docker compose up
```

## Limpeza

```sh
docker compose down --volumes --rmi all
```

## Api

```sh
ENDPOINT_URL="http://localhost:8080/"
curl -X GET  \
    --user "airflow:airflow" \
    "${ENDPOINT_URL}/api/v1/pools"
```

# Atualizando de componentes ou bibliotecas

Qualquer alteração pode ser feita diretamente no requirements.txt, e depois rode o docker build. Alem de libs o ubuntu podem ser feitas diretamente no Dockerfile.