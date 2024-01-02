--https://leetcode.com/problems/calculate-salaries/

/* Write your PL/SQL query statement below */
with cte_max_sal as
(
    select company_id, max(salary) max_sal
        from salaries
        group by company_id
)
select a.company_id, a.employee_id, a.employee_name,
       case
            when max_sal < 100
                then a.salary
            when max_sal between 1000 and 10000
                then round(salary - salary * .24, 0)
            when max_sal > 10000
                then round(salary - salary * .49, 0)
            else a.salary
       end salary
    from salaries a
    join
         cte_max_sal b
    on (a.company_id = b.company_id)