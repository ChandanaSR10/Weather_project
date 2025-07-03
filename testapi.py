import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 12.9788,
    "longitude": 77.6581,
    "daily": ["sunrise", "sunset", "rain_sum", "temperature_2m_max", "temperature_2m_min", "sunshine_duration", "daylight_duration", "precipitation_hours"],
    "hourly": ["temperature_2m", "rain", "relative_humidity_2m", "snowfall", "visibility", "wind_direction_10m", "wind_speed_10m", "soil_temperature_0cm", "uv_index", "sunshine_duration"],
    "timezone": "America/New_York",
    "forecast_days": 1
}

response = requests.get(url, params=params, verify=False)

# Print raw JSON
print(response.json())
