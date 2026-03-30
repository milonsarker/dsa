# https://leetcode.com/problems/find-bursty-behavior/
# Write your MySQL query statement below

with weekly_avg as 
(
    select user_id, count(*)/4 avg_weekly_posts
        from posts
        where post_date between '2024-02-01' and '2024-02-28'
        group by user_id
), 
daily_count as 
(
    select user_id, post_date, count(*) daily_post
        from posts
        where post_date between '2024-02-01' and '2024-02-28'
        group by user_id, post_date
), 
seven_day_window as 
(
    select  user_id,
            post_date, 
            sum(daily_post) over (partition by user_id order by post_date range between interval 6 day preceding and current row) as seven_day_count
        from daily_count
)
select a.user_id, max(seven_day_count) max_7day_posts, b.avg_weekly_posts
    from seven_day_window a 
    join weekly_avg b
    on (a.user_id = b.user_id)
    where a.seven_day_count >= b.avg_weekly_posts * 2
    group by a.user_id, b.avg_weekly_posts
    order by user_id
    ;