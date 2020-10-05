# Write your MySQL query statement below
select *
from cinema
where description<>"boring" and id%2!=0
ORDER BY rating DESC