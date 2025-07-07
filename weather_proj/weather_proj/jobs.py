from dagster import define_asset_job, AssetSelection
from weather_proj.assets import fetch_weather_api_data, write_to_azure_blob

hourly_weather_job_ingestion = define_asset_job(
    name="hourly_weather_job",
    selection=AssetSelection.assets(fetch_weather_api_data, write_to_azure_blob)
)
