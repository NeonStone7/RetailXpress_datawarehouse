{% test assert_large_values(model, column_name) %}

select *
from {{ model }}
where length({{ column_name }}) > 30

{% endtest %}