select 
distinct
string_field_0 as product_id,
string_field_1 as description,
string_field_2 as specifications,
string_field_3 as images,
current_timestamp as ingestion_timestamp
from {{ source('raw_product_metadata', 'product_metadata') }}
where string_field_0 <> 'product_id'
and string_field_0 is not null