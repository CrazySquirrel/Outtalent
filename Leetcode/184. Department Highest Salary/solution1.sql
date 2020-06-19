# Write your MySQL query statement below
select
    Department.name as 'Department',
    Employee.name as 'Employee',
    Salary
from
    Employee join Department on Employee.DepartmentId = Department.Id
where
    (Employee.DepartmentId , Salary) in
    (   select
            DepartmentId, max(Salary)
        from
            Employee
        group by DepartmentId
	)
;