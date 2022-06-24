--https://leetcode.com/problems/the-change-in-global-rankings/


/* Write your PL/SQL query statement below */
with cte_cur_rnk as
(
    select a.*, rank() over (order by points desc , name asc) rnk
        from teampoints a
),
cte_upd_rnk as
(
    select a.*, rank() over (order by points desc, name asc) rnk
        from (
                select a.team_id, a.name, a.points + b.points_change points
                    from teamPoints a
                    join
                         pointsChange b
                    on (a.team_id = b.team_id)
             ) a
)
select a.team_id, a.name, b.rnk  - a.rnk rank_diff
    from cte_upd_rnk a
    join
         cte_cur_rnk b
    on (a.team_id = b.team_id);