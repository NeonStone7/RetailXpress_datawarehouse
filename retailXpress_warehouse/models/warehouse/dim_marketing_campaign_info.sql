select
campaign_id, 
campaign_name,
channels,
start_date,
end_date,
current_timestamp as ingestion_timestamp

from {{ ref('stg_marketing_campaigns') }}