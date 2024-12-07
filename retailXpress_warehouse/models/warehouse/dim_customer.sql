select
 
distinct
cust.customer_id,
name,
email,
phone,
pref.preferred_categories,
pref.spending_patterns,
current_timestamp as ingestion_timestamp

from {{ ref('stg_customer')}} cust
left join {{ ref('stg_customer_preferences') }} pref
 on cust.customer_id = pref.customer_id