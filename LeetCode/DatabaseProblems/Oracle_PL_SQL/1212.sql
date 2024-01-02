--https://leetcode.com/problems/team-scores-in-football-tournament/

/* Write your PL/SQL query statement below */
with cte_a_team as
(
    select host_team , sum(
                                case
                                    when host_goals = guest_goals then 1
                                    when host_goals > guest_goals then 3
                                    else 0
                                end
                          ) points
        from matches
        group by host_team
),
cte_b_team as
(
    select guest_team , sum(
                                case
                                    when host_goals = guest_goals then 1
                                    when host_goals < guest_goals then 3
                                    else 0
                                end
                          ) points
        from matches
        group by guest_team
)
select a.team_id, a.team_name, nvl(sum(b.points),0) num_points
    from teams a
    left join
        (
            select host_team team , points from cte_a_team
            union all
            select guest_team team, points from cte_b_team
        ) b
    on (a.team_id = b.team)
    group by a.team_id, a.team_name
    order by num_points desc,  team_id asc ;