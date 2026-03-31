#https://leetcode.com/problems/viewers-turned-streamers/
select a.user_id, count(*) sessions_count
    from (select *, rank() over (partition by user_id order by session_start ) as rnk  from sessions ) a
    join sessions b
    on (a.user_id = b.user_id and a.session_start <= b.session_start)
    where a.rnk =1 and a.session_type = 'Viewer' and  b.session_type = 'Streamer'
    group by 1
    order by  count(*) desc, user_id desc
    ;
