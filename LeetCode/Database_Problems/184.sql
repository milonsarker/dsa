/* Write your PL/SQL query statement below */
with max_sal as
(
    select departmentid, max(salary) max_s
        from employee
        group by departmentid
)
select distinct c.name department, a.name employee, b.max_s salary
    from employee a
    join
         max_sal b
    on (a.salary = b.max_s and a.departmentid = b.departmentid)
        join
         department c
     on (b.departmentid = c.id)