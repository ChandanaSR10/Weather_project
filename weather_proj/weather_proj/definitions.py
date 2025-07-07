# weather_proj/definitions.py

from dagster import Definitions, load_assets_from_modules
from dagster_dbt import load_assets_from_dbt_project
import os

from weather_proj import assets
from weather_proj.jobs import hourly_weather_job_ingestion
from weather_proj.schedules import hourly_weather_schedule
from weather_proj.resources import dbt_resource

# --- Ingestion Assets ---
ingestion_assets = load_assets_from_modules([assets], group_name="ingestion")

# --- dbt Transformation Assets ---
dbt_assets = load_assets_from_dbt_project(
    project_dir=os.path.join("..", "weather_transform"),
    profiles_dir=os.path.join("..", "weather_transform"),
    key_prefix=["transformation"],  # Optional: to namespace dbt models
)

# --- Dagster Definitions ---
defs = Definitions(
    assets=ingestion_assets + dbt_assets,
    jobs=[hourly_weather_job_ingestion],
    schedules=[hourly_weather_schedule],
    resources={"dbt": dbt_resource},
)
