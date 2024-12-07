select 
distinct
string_field_0 as  store_id,
string_field_1 as store_name,
string_field_2 as city,
string_field_3 as region,
current_timestamp as ingestion_timestamp
from {{ source('raw_stores', 'stores')}}

where string_field_0 is not null