select 
distinct
string_field_0 as supplier_id,
string_field_1 as name,
string_field_2 as contact_info,
current_timestamp as ingestion_timestamp

from {{ source('raw_suppliers', 'suppliers')}}
where string_field_0 <> 'supplier_id'
and string_field_0 is not null