#https://leetcode.com/problems/employees-with-deductions/description/



# Write your MySQL query statement below
with cte_wh as
(
    select employee_id, sum(ceil((timestampdiff(second,  in_time, out_time))/60)) minutes
        from logs
        group by employee_id
)
select b.employee_id
    from cte_wh a
    right join employees b
    on (a.employee_id = b.employee_id)
    where (b.needed_hours * 60) > ifnull(a.minutes,0);