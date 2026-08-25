from datetime import datetime

try:
    from airflow import DAG
    from airflow.operators.bash import BashOperator

    with DAG(
        dag_id="portfolio_etl_pipeline",
        start_date=datetime(2026, 1, 1),
        schedule=None,
        catchup=False,
        tags=["portfolio", "etl"],
    ) as dag:
        run_pipeline = BashOperator(
            task_id="run_pipeline",
            bash_command="python src/load.py",
        )
except ImportError:
    # Allows the repository to remain readable without Airflow installed.
    pass
