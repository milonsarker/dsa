#https://leetcode.com/problems/activity-participants/description/


# Write your MySQL query statement below
with cte_cnt as
(
    select activity, count(*) cnt
        from friends
        group by activity
),
cte_min_max as
(
    select min(cnt) min_cnt, max(cnt) max_cnt
        from cte_cnt
)
select activity
    from cte_cnt
    where cnt not in (select min_cnt from cte_min_max union select max_cnt from cte_min_max)