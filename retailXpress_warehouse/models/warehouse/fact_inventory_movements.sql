select
movement_id, 
product_id,
sup.supplier_id,
store_id,
quantity,
current_timestamp as ingestion_timestamp

from {{ ref('stg_inventory_movements') }} invt
left join {{ ref('stg_suppliers') }} sup
on invt.supplier_id = sup.supplier_id
