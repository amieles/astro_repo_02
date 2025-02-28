from airflow.decorators import dag
from datetime import datetime, timedelta
from airflow.providers.snowflake.operators.snowflake import SnowflakeQueryOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
@dag(
    "example_test_query",
    start_date=datetime(2020, 6, 1),
    max_active_runs=3,
    schedule="@daily",
    default_args=default_args,
    template_searchpath="/usr/local/airflow/include/sql/",
    catchup=False,
)
def call_snowflake_scripts():
    opr_call_script = SnowflakeQueryOperator(
        task_id="call_test1",
        snowflake_conn_id="snowflake_conn",
        sql="test_query.sql"
    )

    opr_call_script

call_snowflake_scripts()






