--https://leetcode.com/problems/find-latest-salaries/description/

select emp_id, firstname, lastname, max(salary) salary, department_id
    from salary
    group by emp_id, firstname, lastname, department_id
    order by 1;