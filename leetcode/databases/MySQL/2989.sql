--https://leetcode.com/problems/class-performance/

-- Write your MySQL query statement below
with cte_sum as 
(
    select student_id, sum(assignment1 + assignment2 + assignment3) scr
        from scores
        group by 1
)
    select max(scr) - min(scr) difference_in_score
        from cte_sum;