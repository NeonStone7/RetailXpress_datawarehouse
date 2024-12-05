{% test assert_empty_or_small_values(model, column_name) %}

select *
from {{ model }}
where length({{ column_name }}) <= 3

{% endtest %}