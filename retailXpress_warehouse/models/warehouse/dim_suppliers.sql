select 
 
distinct
supplier_id,
name,
contact_info,
current_timestamp as ingestion_timestamp

from {{ ref('stg_suppliers')}}
