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

#  Window Fuctions

with cte_win as
(
    select  user_id, steps_date,
            round(avg(steps_count) over(partition by user_id order by steps_date rows between 2 preceding and current row), 2) as rolling_average, 
            lag(steps_date, 2) over(partition by user_id order by steps_date) as two_dates_before
        from steps
)
select user_id, steps_date, rolling_average
    from cte_win
    where datediff(steps_date, two_dates_before) = 2
    order by user_id, steps_date
    ;