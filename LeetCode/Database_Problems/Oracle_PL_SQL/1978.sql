--https://leetcode.com/problems/employees-whose-manager-left-the-company/

/* Write your PL/SQL query statement below */
select distinct a.employee_id
    from employees a
    left join
         employees b
    on (a.manager_id = b.employee_id)
    where a.salary < 30000 and b.employee_id is null and a.manager_id is not null
    order by 1;