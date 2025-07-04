import dagster as dg
import requests
import json
from azure.storage.blob import BlobServiceClient
import json, datetime
import os

@dg.asset
def fetch_weather_api_data(context) -> dict:
    import requests

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 12.9788,
        "longitude": 77.6581,
        "daily": ["sunrise", "sunset", "rain_sum", "temperature_2m_max"],
        "hourly": ["temperature_2m", "rain", "uv_index"],
        "timezone": "Asia/Kolkata",
        "forecast_days": 1
    }

    response = requests.get(url, params=params, verify=False)
    data = response.json()  # This is your raw JSON as Python dict
    context.log.info("Fetched data from API")
    return data  # Return raw JSON

@dg.asset(deps=[fetch_weather_api_data])
def write_to_azure_blob(context, fetch_weather_api_data: dict) -> str:
    blob_conn_str = "DefaultEndpointsProtocol=https;AccountName=weatherraw25;AccountKey=k9dFJHtS3ZKrOwdY91ETEmNnUfLZotS25781iumemfDGfsxv5olQA8KyTpTdNDOdj3Iq8s7Trqpp+ASteaFlAQ==;EndpointSuffix=core.windows.net"
    container = "rawweatherdata"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    file_name = f"weather-{timestamp}.json"

    blob_service = BlobServiceClient.from_connection_string(blob_conn_str)
    blob_client = blob_service.get_container_client(container).get_blob_client(file_name)

    blob_client.upload_blob(json.dumps(fetch_weather_api_data), overwrite=True)
    context.log.info(f"Wrote to blob: {file_name}")
    return file_name

import dagster as dg
from azure.storage.blob import BlobServiceClient
import json
import datetime
import snowflake.connector






