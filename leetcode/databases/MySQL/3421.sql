# https://leetcode.com/problems/find-students-who-improved/

# Write your MySQL query statement below
with cte_rnk as 
(
select  * , rank() over (partition by student_id, subject order by exam_date) frnk, 
            rank() over (partition by student_id, subject order by exam_date desc) lrnk
    from scores 
)
select a.student_id, a.subject, a.score first_score, b.score latest_score  
    from cte_rnk a 
    join cte_rnk b 
    on (a.student_id = b.student_id and a.subject =b.subject and a.frnk = b.lrnk and a.exam_date < b.exam_date)
    where b.score > a.score
    and a.frnk = 1
    and b.lrnk = 1
    ;

