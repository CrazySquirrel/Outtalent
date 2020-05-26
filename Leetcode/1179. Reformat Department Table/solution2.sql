# Write your MySQL query statement below

select
    distinct id,
    max(case month when 'Jan' then revenue end) as 'Jan_Revenue',
    max(case month when 'Feb' then revenue end) as 'Feb_Revenue',
    max(case month when 'Mar' then revenue end) as 'Mar_Revenue',
    max(case month when 'Apr' then revenue end) as 'Apr_Revenue',
    max(case month when 'May' then revenue end) as 'May_Revenue',
    max(case month when 'Jun' then revenue end) as 'Jun_Revenue',
    max(case month when 'Jul' then revenue end) as 'Jul_Revenue',
    max(case month when 'Aug' then revenue end) as 'Aug_Revenue',
    max(case month when 'Sep' then revenue end) as 'Sep_Revenue',
    max(case month when 'Oct' then revenue end) as 'Oct_Revenue',
    max(case month when 'Nov' then revenue end) as 'Nov_Revenue',
    max(case month when 'Dec' then revenue end) as 'Dec_Revenue'
from Department
group by id