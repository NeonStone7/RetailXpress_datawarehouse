select 
distinct
campaign_id,
campaign_name,
channels,
start_date,
end_date,
split(split(performance_metrics, ',')[0], ':')[1] as click_through_rate,
split(split(performance_metrics, ',')[1], ':')[1] as conversion_rate,
replace(split(split(performance_metrics, ',')[2], ':')[1], '}', '') as roi,
current_timestamp as ingestion_timestamp

from {{ source('raw_marketing_campaigns', 'marketing_campaigns') }}
where campaign_id is not null
