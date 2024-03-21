from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "Prashantvik",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="cron_expression_dag",
    description="DAG example of how cron can be used to schedule in airflow",
    start_date=datetime(2024, 3, 5),
    default_args=default_args,
    schedule_interval="@daily",
) as dag:

    task1 = BashOperator(
        task_id="simple_task",
        bash_command="echo This dag represents how dags can be scheduled with cron expression, runs daily and has a start_date of March 5th, created on March 9th. Backfill and catcup concept was being used.",
    )


with DAG(
    dag_id="cron_expression_dag_2",
    description="DAG example of how cron can be used to schedule in airflow",
    start_date=datetime(2024, 3, 7),
    default_args=default_args,
    schedule_interval="0 15 * * Tue-Fri",
) as dag:

    task1 = BashOperator(
        task_id="simple_task",
        bash_command="echo This dag represents how dags can be scheduled with cron expression. Runs at 15:00 on every day-of-week from Tuesday through Friday.",
    )
