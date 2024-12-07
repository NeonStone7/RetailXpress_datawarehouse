select
distinct
dim_s.delivery_id,
dim_s.status,
fact_s.supplier_id,
fact_s.product_id,
fact_s.quantity,
dim_sup.name as supplier_name,
dim_sup.contact_info,
prod.product_id,
prod.name as product_name, 
prod.category,
prod.price,
prod.stock_level,
prod.description,
prod.specifications,
prod.images,
current_timestamp as ingestion_timestamp

from {{ ref('dim_supplier_deliveries') }} dim_s
left join {{ ref('fact_supplier_deliveries') }} fact_s
    on dim_s.delivery_id = fact_s.delivery_id
left join {{ ref('dim_suppliers')}} dim_sup
    on dim_sup.supplier_id = fact_s.supplier_id
left join {{ ref('dim_products') }} prod
    on prod.product_id = fact_s.product_id
