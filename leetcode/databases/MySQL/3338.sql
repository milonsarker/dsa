# https://leetcode.com/problems/second-highest-salary-ii/
# Write your MySQL query statement below

with cte_rnk as 
(
    select *, dense_rank () over (partition by dept order by salary desc) rnk 
        from employees
)
select emp_id, dept
    from cte_rnk
    where rnk = 2
    order by emp_id asc
    ;