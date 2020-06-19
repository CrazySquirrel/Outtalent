# Write your MySQL query statement below
select t.Request_at Day, round(sum(case when t.Status like 'cancelled%' then 1 else 0 end)/count(*), 2) 'Cancellation Rate'
FROM Trips t JOIN Users u ON t.Client_Id = u.Users_Id AND u.Banned = 'No'
where t.Request_at between '2013-10-01' and '2013-10-03' group by t.Request_at;