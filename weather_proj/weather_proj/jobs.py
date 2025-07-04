import dagster as dg
from weather_proj.assets import fetch_weather_api_data
from weather_proj.assets import write_to_azure_blob  # ✅ Fixed

hourly_weather_job_ingestion = dg.define_asset_job(
    name="hourly_weather_job",
    selection=dg.AssetSelection.assets("fetch_weather_api_data", "write_to_azure_blob")
)
from dagster import define_asset_job, AssetSelection

