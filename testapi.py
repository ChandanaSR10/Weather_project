import requests
import json

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

# Get the raw JSON data
data = response.json()

# Print it (just like before)
print(data)

# Save the raw JSON data to a file
with open("weather_full.json", "w") as f:
    json.dump(data, f, indent=2)

print(" JSON saved to weather_full.json")
