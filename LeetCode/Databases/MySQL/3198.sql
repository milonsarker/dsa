#https://leetcode.com/problems/find-cities-in-each-state/description/

# Write your MySQL query statement below
select state, group_concat(city order by city separator ', ') as cities
    from cities
    group by state
    order by state;