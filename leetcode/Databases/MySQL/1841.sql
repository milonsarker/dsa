#https://leetcode.com/problems/league-statistics/description/


# Write your MySQL query statement below
with cte_u as
(
    select home_team_id tid, 'h' type,  home_team_goals, away_team_goals
        from matches
    union all
    select away_team_id tid, 'a' type,  home_team_goals, away_team_goals
        from matches
),
cte_summ as
(
    select tid, count(*) matches_played, sum(case when type = 'h' then home_team_goals else away_team_goals end) goal_for,
           sum(case when type = 'h' then  away_team_goals  else home_team_goals end) goal_against,
           sum(case when type = 'h' and  home_team_goals > away_team_goals  then 3
                    when type = 'h' and  home_team_goals < away_team_goals then 0
                    when type = 'a' and  home_team_goals < away_team_goals  then 3
                    when type = 'a' and  home_team_goals > away_team_goals then 0
                    else 1 end) points
        from cte_u
        group by tid
)
select b.team_name, matches_played, points, goal_for, goal_against, goal_for - goal_against goal_diff
    from cte_summ a
    join
         teams b
    on (b.team_id = a.tid)
    order by points desc, goal_diff desc, team_name;