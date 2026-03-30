--https://leetcode.com/problems/new-users-daily-count/

/* Write your PL/SQL query statement below */
with cte_first_login as
(select user_id , min(activity_date) first_login
    from traffic
    where activity = 'login'
    group by user_id
)
select to_char(first_login,'yyyy-mm-dd') login_date, count(user_id) user_count
    from cte_first_login
    where first_login between to_date('2019-06-30') - 90 and to_date('2019-06-30')
    group by to_char(first_login,'yyyy-mm-dd')
    ;