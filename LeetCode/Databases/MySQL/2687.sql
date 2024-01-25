--https://leetcode.com/problems/bikes-last-time-used/
-- Write your MySQL query statement below
select bike_number, max(end_time) end_time
    from bikes
    group by 1
    order by 2 desc;