from dagster_dbt import dbt_cli_resource
import os

dbt_resource = dbt_cli_resource.configured({
    "project_dir": os.path.join("..", "weather_transform"),  # relative to your Dagster module
    "profiles_dir": os.path.join("..", "weather_transform")  # same here
})
