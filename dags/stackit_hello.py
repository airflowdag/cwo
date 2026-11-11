from datetime import datetime

from airflow import DAG

try:
    from airflow.providers.standard.operators.bash import BashOperator
    from airflow.providers.standard.operators.python import PythonOperator
except ImportError:
    from airflow.operators.bash import BashOperator
    from airflow.operators.python import PythonOperator


def _hello():
    print("hello from CWO on STACKIT")


with DAG(
    dag_id="stackit_hello",
    start_date=datetime(2026, 11, 1),
    schedule=None,
    catchup=False,
    tags=["stackit", "smoke"],
) as dag:
    bash = BashOperator(task_id="bash_hello", bash_command="echo hello; hostname; date -u")
    py = PythonOperator(task_id="python_hello", python_callable=_hello)
    bash >> py
