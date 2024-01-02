#https://leetcode.com/problems/compute-the-rank-as-a-percentage/description/


# Write your MySQL query statement below
with cte_rank as
(
    select student_id, department_id, rank() over(partition by department_id order by mark desc) student_rank_in_the_department
        from students
),
cte_count as
(
    select department_id, count(*) the_number_of_students_in_the_department
        from students
        group by department_id
)
select a.student_id, b.department_id, ifnull(round((student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_the_department - 1), 2),0.00) percentage
    from cte_rank a
    left join cte_count b
    on (a.department_id = b.department_id);