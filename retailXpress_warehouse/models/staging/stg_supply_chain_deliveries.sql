select *,
current_timestamp as ingestion_timestamp

from {{ source('raw_supply_chain_deliveries', 'supply_chain_deliveries') }}