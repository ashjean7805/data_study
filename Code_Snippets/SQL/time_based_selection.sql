-- datetime based
with 
    test
as (
    select cast('2023-04-23 12:00:00' as datetime) as db_datetime
         , 1 as sample_type
    union all
    select cast('2023-04-23 13:00:00' as datetime), 2
    union all
    select cast('2023-04-23 14:00:00' as datetime), 3
)
select substring(min(concat(substring(cast(db_datetime as string),1,19),sample_type)),20) as sample_type
from test


