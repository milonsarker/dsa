--https://leetcode.com/problems/students-and-examinations/

select distinct st.student_id,
       st.student_name,
       su.subject_name,
       count(ex.student_id) over(partition by st.student_id, su.subject_name) attended_exams
from students st cross join subjects su
     left join examinations ex
     on ex.student_id =st.student_id
        and ex.subject_name = su.subject_name
order by 1, 2