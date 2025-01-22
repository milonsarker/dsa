# https://leetcode.com/problems/find-cities-in-each-state-ii/

# Write your MySQL query statement below

select state, group_concat(city order by city asc separator ', ' ) cities, 
       sum(case when substr(state, 1, 1) = substr(city, 1, 1) then 1 else 0 end) matching_letter_count
    from cities
    group by state
    having sum(case when substr(state, 1, 1) = substr(city, 1, 1) then 1 else 0 end) > 0 and count(*) >= 3
    order by matching_letter_count desc, state
    ;