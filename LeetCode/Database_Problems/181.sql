--https://leetcode.com/problems/employees-earning-more-than-their-managers/

/* Write your PL/SQL query statement below */
select a.name employee
    from employee a
    join
         employee b
    on (b.id = a.managerid)
    where a.salary > b.salary