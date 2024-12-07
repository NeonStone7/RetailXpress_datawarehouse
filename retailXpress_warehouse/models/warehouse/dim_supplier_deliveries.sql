select
delivery_id,
delivery_date,
status,
current_timestamp as ingestion_timestamp

from {{ ref('stg_supply_chain_deliveries') }}