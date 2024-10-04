# https://leetcode.com/problems/find-top-scoring-students/

# Write your MySQL query statement below

with cte_count as 
(
    select a.student_id, grade, count(a.course_id) over (partition by student_id, c.major) d_count
        from enrollments a 
        join courses b 
        on (a.course_id = b.course_id)
        join students c 
        on (a.student_id = c.student_id and b.major = c.major)
        where grade = 'A'
), 
course_count as 
(
    select student_id, count(*) course_count
        from courses a 
        join students b
        on (a.major = b.major)
        group by student_id
)

select distinct a.student_id 
    from cte_count a 
    join course_count b
    on (a.student_id = b.student_id)
    where (a.d_count = b.course_count)
    order by student_id
    ;

