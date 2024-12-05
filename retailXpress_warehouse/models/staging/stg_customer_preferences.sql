select 
distinct
string_field_0 as customer_id,
string_field_1 as preferred_categories,
string_field_2 as spending_patterns,
current_timestamp as ingestion_timestamp

from {{ source('raw_customer_preferences', 'customer_preferences') }}
where string_field_0 <> 'customer_id'
and string_field_0 is not null