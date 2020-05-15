# Write your MySQL query statement below

SELECT
    distinct id,
    MAX(CASE month WHEN 'Jan' THEN revenue END) AS 'Jan_Revenue',
    MAX(CASE month WHEN 'Feb' THEN revenue END) AS 'Feb_Revenue',
    MAX(CASE month WHEN 'Mar' THEN revenue END) AS 'Mar_Revenue',
    MAX(CASE month WHEN 'Apr' THEN revenue END) AS 'Apr_Revenue',
    MAX(CASE month WHEN 'May' THEN revenue END) AS 'May_Revenue',
    MAX(CASE month WHEN 'Jun' THEN revenue END) AS 'Jun_Revenue',
    MAX(CASE month WHEN 'Jul' THEN revenue END) AS 'Jul_Revenue',
    MAX(CASE month WHEN 'Aug' THEN revenue END) AS 'Aug_Revenue',
    MAx(CASE month WHEN 'Sep' THEN revenue END) AS 'Sep_Revenue',
    MAX(CASE month WHEN 'Oct' THEN revenue END) AS 'Oct_Revenue',
    MAX(CASE month WHEN 'Nov' THEN revenue END) AS 'Nov_Revenue',
    MAX(CASE month WHEN 'Dec' THEN revenue END) AS 'Dec_Revenue'
FROM Department
GROUP BY id