{{ config(materialized='table', schema='analytics') }}

with stg as (
    select *
    from {{ ref('stg_weather_data') }}
),

exploded as (
    select
        date,
        value::timestamp as hour_time,
        stg.hourly_temperatures[index]::float as temperature,
        stg.hourly_uv[index]::float as uv_index,
        stg.hourly_rain[index]::float as rain
    from stg,
    lateral flatten(input => stg.hourly_times) as f
    qualify row_number() over (partition by date order by f.index) <= array_size(stg.hourly_times)
),

aggregated as (
    select
        date,
        avg(temperature) as avg_temperature,
        max(temperature) as max_hourly_temp,
        max(uv_index) as peak_uv_index,
        sum(rain) as total_hourly_rain,
        max_by(hour_time, uv_index) as peak_uv_time
    from exploded
    group by date
)

select
    s.date,
    s.daily_temperature_max,
    a.avg_temperature,
    a.max_hourly_temp,
    s.daily_rain_sum,
    a.total_hourly_rain,
    a.peak_uv_index,
    a.peak_uv_time,
    s.sunrise,
    s.sunset,
    s.latitude,
    s.longitude,
    s.elevation,
    s.timezone
from stg s
join aggregated a on s.date = a.date
