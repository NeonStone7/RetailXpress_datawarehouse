select
movement_id, 
movement_date,
movement_type,
current_timestamp as ingestion_timestamp

from {{ ref('stg_inventory_movements') }}
