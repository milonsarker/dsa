--https://leetcode.com/problems/game-play-analysis-iv/

with cte_min_date as
(
    select player_id , event_date , min(event_date) over ( partition by player_id ) min_date
        from activity
)
select round(count(case when event_date = min_date + 1 then 1 else null end) / count(distinct player_id),2) fraction
    from cte_min_date