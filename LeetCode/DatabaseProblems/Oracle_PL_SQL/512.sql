--https://leetcode.com/problems/game-play-analysis-ii/

/* Write your PL/SQL query statement below */
with cte_min_date as
(
    select player_id, min(event_date) event_date
        from activity
        group by player_id
)
select a.player_id, a.device_id
    from activity a
    join
         cte_min_date b
    on (a.player_id = b.player_id and a.event_date = b.event_date)