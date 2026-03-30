--https://leetcode.com/problems/reported-posts-ii/

/* Write your PL/SQL query statement below */

with cte_avg_removal as
(
    select action_date, (count( distinct b.post_id)/count(distinct a.post_id)) * 100 avg_removal
        from (
                select post_id, action, action_date
                    from actions
                    where action = 'report' and extra = 'spam'
             ) a
        left join
             removals b
        on (a.post_id = b.post_id)
        group by action_date
)
select round(avg(avg_removal), 2) average_daily_percent
    from cte_avg_removal;