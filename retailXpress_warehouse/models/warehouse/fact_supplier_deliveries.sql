select
delivery_id,
supplier_id,
product_id,
quantity,
current_timestamp as ingestion_timestamp

from {{ ref('stg_supply_chain_deliveries') }}