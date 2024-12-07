select
campaign_id, 
click_through_rate,
conversion_rate,
roi,
current_timestamp as ingestion_timestamp


from {{ ref('stg_marketing_campaigns') }}