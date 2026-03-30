#https://leetcode.com/problems/premier-league-table-ranking/


# Write your MySQL query statement below
with cte_points as 
(
    select team_id, team_name, (wins * 3 + draws * 1 ) points
        from TeamStats
        group by team_id, team_name 
), 
cte_rank as 
(
    select *, rank() over (order by points desc) as position
        from cte_points
)
select * 
    from cte_rank
    order by position, team_name asc