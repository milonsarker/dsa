--https://leetcode.com/problems/project-employees-ii/

/* Write your PL/SQL query statement below */
with cte_proj_cnt as
(
    select project_id, count(employee_id) emp_cnt
        from project
        group by project_id
)
select project_id
    from cte_proj_cnt
    where emp_cnt in (select max(emp_cnt) from cte_proj_cnt);