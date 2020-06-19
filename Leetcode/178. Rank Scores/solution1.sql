# Write your MySQL query statement below
select s.Score, count(distinct t.Score) as 'Rank'
from Scores s join Scores t on s.Score <= t.Score
group by s.Id order by s.Score desc;