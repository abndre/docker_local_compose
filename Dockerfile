FROM apache/airflow:2.6.0-python3.10
ADD requirements.txt .
RUN pip install -r requirements.txt

