#https://leetcode.com/problems/find-peak-calling-hours-for-each-city/
with cte_cnt as 
(
    select city, hour(call_time) peak_calling_hour, count(*)  cnt 
        from calls
        group by city, hour(call_time)
), 
cte_rnk as 
(
    select *, dense_rank() over(partition by city order by cnt desc) as rnk
        from cte_cnt
)
select city, peak_calling_hour, cnt number_of_calls
    from cte_rnk
    where rnk = 1
    order by peak_calling_hour desc, city desc