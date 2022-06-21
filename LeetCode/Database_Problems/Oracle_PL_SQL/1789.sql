--https://leetcode.com/problems/primary-department-for-each-employee/

/* Write your PL/SQL query statement below */
with cte_y as
(
    select distinct employee_id , department_id
        from employee
        where primary_flag = 'Y'
)
select *
    from cte_y
union
select distinct employee_id , department_id
    from employee
    where employee_id not in (select employee_id from cte_y);