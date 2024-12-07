select 
product_id,
name,
category,
price,
stock_level,
current_timestamp as ingestion_timestamp

from {{ source('raw_products', 'products')}}