--https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/

/* Write your PL/SQL query statement below */
with cte_cnt as
(
    select user_id, count(distinct session_id) sess_cnt
        from activity
        where trunc(activity_date) between to_date('27-07-2019','dd-mm-yyyy') -29 and to_date('27-07-2019','dd-mm-yyyy')
        group by user_id
)
select nvl(round(sum(sess_cnt)/count( distinct user_id), 2), 0.00) average_sessions_per_user
    from cte_cnt