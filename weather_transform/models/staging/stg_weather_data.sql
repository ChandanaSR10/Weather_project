{{ config(materialized='table', schema='analytics') }}

with raw as (
    select
        try_parse_json($1):daily.time[0]::date as date,
        try_parse_json($1):daily.temperature_2m_max[0]::float as daily_temperature_max,
        try_parse_json($1):daily.rain_sum[0]::float as daily_rain_sum,
        try_parse_json($1):daily.sunrise[0]::timestamp as sunrise,
        try_parse_json($1):daily.sunset[0]::timestamp as sunset,
        try_parse_json($1):elevation::float as elevation,
        try_parse_json($1):latitude::float as latitude,
        try_parse_json($1):longitude::float as longitude,
        try_parse_json($1):timezone::string as timezone,
        try_parse_json($1):hourly.time as hourly_times,
        try_parse_json($1):hourly.temperature_2m as hourly_temperatures,
        try_parse_json($1):hourly.uv_index as hourly_uv,
        try_parse_json($1):hourly.rain as hourly_rain
    from {{ source('raw', 'weather_raw') }}
    where try_parse_json($1) is not null
)

select * from raw
