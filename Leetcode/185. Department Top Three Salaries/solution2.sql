# Write your MySQL query statement bel
select c.Name Department, a.Name Employee, a.Salary
from Employee a
left join Employee b on a.DepartmentId = b.DepartmentId and a.Salary < b.Salary
inner join Department c on a.DepartmentId = c.Id
group by a.Id
having count(distinct b.Salary) + 1 <= 3
