select 
distinct
customer_id,
name,
email,
case when left(phone, 2) = '00' then replace(phone, left(phone, 2), '+') else phone end as phone,
loyalty_points,
join_date,
current_timestamp as ingestion_timestamp

from {{ source('raw_customers', 'customers')}}
where customer_id is not null