--https://leetcode.com/problems/total-traveled-distance/

with cte_dist as 
(
    select user_id, sum(distance) dist
        from rides 
        group by user_id
)
select a.user_id, a.name, ifnull(b.dist, 0)  as traveled_distance
    from users a
    left join cte_dist b
    on (a.user_id = b.user_id)
    order by a.user_id