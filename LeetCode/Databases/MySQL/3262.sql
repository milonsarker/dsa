# https://leetcode.com/problems/find-overlapping-shifts/

# Write your MySQL query statement below

select a.employee_id, count(*) overlapping_shifts
    from EmployeeShifts a 
    join EmployeeShifts b on (a.employee_id = b.employee_id)
    where a.start_time < b.start_time and a.end_time > b.start_time
    group by a.employee_id
    ;