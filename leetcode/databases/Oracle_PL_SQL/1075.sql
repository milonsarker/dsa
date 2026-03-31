--https://leetcode.com/problems/project-employees-i/

/* Write your PL/SQL query statement below */
select a.project_id, round(avg(b.experience_years), 2) average_years
    from project a
    join
         employee b
    on (a.employee_id = b.employee_id)
    group by a.project_id