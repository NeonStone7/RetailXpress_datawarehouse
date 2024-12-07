select 
prod.product_id,
prod.name, 
prod.category,
prod.price,
prod.stock_level,
met.description,
met.specifications,
met.images,
current_timestamp as ingestion_timestamp

from {{ ref('stg_products') }} prod
left join  {{ ref('stg_product_metadata') }} met
    on prod.product_id = met.product_id