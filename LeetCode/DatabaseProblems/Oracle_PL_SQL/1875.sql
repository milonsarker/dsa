--https://leetcode.com/problems/group-employees-of-the-same-salary/

/* Write your PL/SQL query statement below */
with cte_emp_cnt as
(
    select salary, count(*) emp_cnt
        from employees
        group by salary
        having count(*) > 1
),
sal_rank as
(
    select salary, emp_cnt, rank() over(order by salary) rnk
        from cte_emp_cnt
)
select b.employee_id, b.name, a.salary, a.rnk team_id
    from sal_rank a
    join
         employees b
    on (a.salary = b.salary)
    order by team_id , b.employee_id;