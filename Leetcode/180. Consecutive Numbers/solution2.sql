# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from logs
where (id + 1, Num) in (select * from logs) and (Id + 2, Num) in (select * from logs)