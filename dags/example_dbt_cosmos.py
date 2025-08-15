# Airflow DAG for running dbt on the dbt project using the duckdb adapter.
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from include.constants import dbt_project_path, venv_execution_config

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={
            "database": "ASTRO_DBT_DEMO",
            "schema": "TEST",
        },
    ),
)

dbt_cosmos_dag = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(dbt_project_path),
    profile_config=profile_config,
    execution_config=venv_execution_config,
    # normal dag parameters
    schedule="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="example_dbt_cosmos",
    # only allow one concurrent run of this DAG, prevents parallel DuckDB calls
    max_active_runs=1,
    concurrency=1,  # only allow a single task execution at a time, prevents parallel DuckDB calls
    is_paused_upon_creation=False,  # start running the DAG as soon as its created
)
