#https://leetcode.com/problems/rolling-average-steps/

select  a.user_id, 
        a.steps_date, 
        round(avg(b.steps_count), 2) rolling_average
    from steps a
    join steps b on (a.user_id = b.user_id and (b.steps_date between a.steps_date - interval 2 day and a.steps_date ))
    group by a.user_id, a.steps_date
    having count(*) = 3
    order by a.user_id, a.steps_date
    ;