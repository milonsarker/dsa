# https://leetcode.com/problems/premier-league-table-ranking-ii/?
# Write your MySQL query statement below

with cte_points as
(
    select team_name, sum(wins * 3 + draws) points
        from teamstats 
        group by team_name
),
cte_rnk as 
(
    select  *, 
            rank() over (order by points desc) as position, 
            ntile(3) over(order by points desc) as tier
            #round(percent_rank() over (order by points desc) * 100.00, 2) tier
        from cte_points
), 
cte_cnt as 
(
    select count(*) tot_cnt
        from teamstats
)
select  team_name,
        points, 
        position, 
        case when position <= ceil(0.33 * tot_cnt) then 'Tier 1'
             when position <= ceil(0.66 * tot_cnt) then 'Tier 2'
             else 'Tier 3'
        end Tier
    from cte_rnk, cte_cnt
    order by position , team_name
    ;