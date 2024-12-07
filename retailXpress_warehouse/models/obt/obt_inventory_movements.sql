select
distinct
dim_inv.movement_id, 
dim_inv.movement_date,
dim_inv.movement_type,
prod.product_id,
prod.name as product_name, 
prod.category,
prod.price,
prod.stock_level,
prod.description,
prod.specifications,
prod.images,
store.store_id,
store.store_name,
store.city,
store.region,
sup.supplier_id,
sup.name as supplier_name,
sup.contact_info,
fact_inv.quantity,
current_timestamp as ingestion_timestamp

from {{ ref('dim_inventory_movements') }} dim_inv
left join {{ ref('fact_inventory_movements') }} fact_inv 
    on dim_inv.movement_id = fact_inv.movement_id
left join  {{ ref('dim_products') }} prod 
    on prod.product_id = fact_inv.product_id
left join {{ ref('dim_stores') }} store
    on store.store_id = fact_inv.store_id
left join {{ ref('dim_suppliers')}} sup
    on sup.supplier_id = fact_inv.supplier_id
