select 
store_id,
store_name,
city,
region,
current_timestamp as ingestion_timestamp

from {{ ref('stg_stores') }}