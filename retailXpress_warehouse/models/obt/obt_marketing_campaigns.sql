select
fact.campaign_id, 
dim.campaign_name,
dim.channels,
dim.start_date,
dim.end_date,
fact.click_through_rate,
fact.conversion_rate,
fact.roi,
current_timestamp as ingestion_timestamp

from {{ ref('fact_marketing_campaigns') }} fact
left join {{ ref('dim_marketing_campaign_info') }} dim
    on fact.campaign_id = dim.campaign_id