# https://leetcode.com/problems/server-utilization-time/

# Write your MySQL query statement below

with cte_end_time as 
(
    select *, lead(status_time, 1) over(partition by server_id order by status_time, session_status) as end_time
        from servers
), 
cte_duration as 
(
    select timestampdiff(second, status_time, end_time) as duration
        from cte_end_time
        where session_status = 'start'
)
select floor(sum(duration)/(24*60*60)) as total_uptime_days
    from cte_duration
    ;
