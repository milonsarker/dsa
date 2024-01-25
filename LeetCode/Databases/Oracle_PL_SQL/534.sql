--https://leetcode.com/problems/game-play-analysis-iii/

/* Write your PL/SQL query statement below */
select player_id, to_char(event_date,'yyyy-mm-dd') event_date,
       sum(games_played) over(partition by player_id order by event_date) games_played_so_far
    from activity;