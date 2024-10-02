# https://leetcode.com/problems/snaps-analysis/
# Write your MySQL query statement below

with cte_tot as 
(
    select b.age_bucket, sum(time_spent) tot_time
        from activities a 
        join age b 
        on (a.user_id = b.user_id)
        group by b.age_bucket
), 
cte_so_time as 
(
    select b.age_bucket, 
            sum(case when a.activity_type = 'open' then time_spent else 0 end) opening_time, 
            sum(case when a.activity_type = 'send' then time_spent else 0 end) sending_time
        from activities a 
        join age b 
        on (a.user_id = b.user_id)
        group by b.age_bucket
)
select  a.age_bucket, 
        round(b.sending_time * 100.00 / a.tot_time, 2)  send_perc, 
        round(b.opening_time * 100.00 / a.tot_time, 2)  open_perc
    from cte_tot a 
    join cte_so_time b
    on (a.age_bucket = b.age_bucket)
