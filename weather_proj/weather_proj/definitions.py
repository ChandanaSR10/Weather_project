# definitions.py
from dagster import Definitions, load_assets_from_modules
from weather_proj import assets
from weather_proj.jobs import hourly_weather_job_ingestion
from weather_proj.schedules import hourly_weather_schedule


defs = Definitions(
    assets=load_assets_from_modules([assets]),
    jobs=[
        hourly_weather_job_ingestion,
    ],
    schedules=[hourly_weather_schedule],
)
