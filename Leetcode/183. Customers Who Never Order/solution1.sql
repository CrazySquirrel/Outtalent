# Write your MySQL query statement below
select Name as 'Customers'
from Customers c
left join Orders o
on c.Id = o.CustomerId
where o.CustomerId is null