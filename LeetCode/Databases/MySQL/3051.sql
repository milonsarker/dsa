# https://leetcode.com/problems/find-candidates-for-data-scientist-position/
# Write your MySQL query statement below

select candidate_id
    from candidates
    group by candidate_id
    having sum(case when skill in ('Python', 'Tableau', 'PostgreSQL') then 1 else 0 end) >= 3
    order by candidate_id
    ;