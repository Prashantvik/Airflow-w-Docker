from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "prashantvik",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="",
    default_args=default_args,
    description="",
    start_date=datetime(),
    schedule_interval="",
    catchup=False,
    tags=[""],
) as dag:

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Hi from bash operator"',
        # env: Optional[Dict[str, str]] = None,
        # output_encoding: str = 'utf-8',
        # skip_exit_code: int = 99,
    )

    python_task = PythonOperator(
        task_id="python_task",
        python_callable=lambda: print("Hi from python operator"),
        # op_kwargs: Optional[Dict] = None,
        # op_args: Optional[List] = None,
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )
