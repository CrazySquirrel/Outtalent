create function getNthHighestSalary(N int) RETURNS INT
BEGIN
    set N=N-1;
    RETURN (
        # Write your MySQL query statement below.
        SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT N,1
    );
END