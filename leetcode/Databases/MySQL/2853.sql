--https://leetcode.com/problems/highest-salaries-difference/

with mkt as 
(
    select 1 jk, max(salary) mkt
        from salaries
        where department = 'Marketing'
        group by department
),
eng as 
(
    select 1 jk, max(salary) eng
        from salaries
        where department = 'Engineering'
        group by department
)
select abs(a.mkt - b.eng) salary_difference
    from mkt a join eng b
    on (a.jk = b.jk)
    ;