--https://leetcode.com/problems/ad-free-sessions/

/* Write your PL/SQL query statement below */
with cte_sess as
(
    select distinct session_id
        from playback a
        join
             ads b
        on (a.customer_id = b.customer_id and b.timestamp between a.start_time and a.end_time)
)
select session_id
    from playback
    where session_id not in (select session_id from cte_sess);