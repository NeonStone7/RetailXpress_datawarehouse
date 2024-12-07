select invt.*,
supch.supplier_id,
current_timestamp  as ingestion_timestamp
from {{ source('raw_inventory_movements', 'inventory_movements') }} invt
left join {{ source('raw_supply_chain_deliveries', 'supply_chain_deliveries') }} supch
    on invt.product_id = supch.product_id

