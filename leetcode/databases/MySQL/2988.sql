#https://leetcode.com/problems/manager-of-the-largest-department/
with cte_cnt as 
(
    select *, count(emp_id) over (partition by dep_id) emp_cnt
        from employees 
), 
cte_ran as 
(
    select * , dense_rank() over(order by emp_cnt desc) as rnk
        from cte_cnt
)
select emp_name as manager_name, dep_id 
    from cte_ran  
    where rnk = 1 and position = 'Manager'
    order by dep_id
    ; 