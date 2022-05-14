--https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

/* Write your PL/SQL query statement below */
select  a.employee_id, a.name, count(*) reports_count, round(avg(b.age)) average_age
    from employees a
    join
         employees b
    on (a.employee_id = b.reports_to)
    group by a.employee_id, a.name
    order by 1