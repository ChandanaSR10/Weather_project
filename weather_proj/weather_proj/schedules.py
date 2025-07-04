from dagster import ScheduleDefinition
from weather_proj.jobs import hourly_weather_job_ingestion

hourly_weather_schedule = ScheduleDefinition(
    job=hourly_weather_job_ingestion,
    cron_schedule="0 * * * *" 
)
