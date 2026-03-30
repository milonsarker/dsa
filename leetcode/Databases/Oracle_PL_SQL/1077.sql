--https://leetcode.com/problems/project-employees-iii/

/* Write your PL/SQL query statement below */
select project_id, employee_id
    from
        (
            select a.project_id, a.employee_id,
                    dense_rank() over( partition by a.project_id order by b.experience_years desc) as rnk
                from project a
                join
                     employee b
                on (a.employee_id = b.employee_id)
        )
    where rnk = 1;