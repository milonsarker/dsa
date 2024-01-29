#https://leetcode.com/problems/flight-occupancy-and-waitlist-analysis/
with cte_cnt as 
(
    select flight_id, count(*) cnt
        from Passengers 
        group by 1
)
select  b.flight_id,
        case when cnt >= capacity then capacity
             when cnt is null then 0
             else cnt end booked_cnt,
        case when cnt > capacity then cnt -capacity 
            else 0 end waitlist_cnt
    from cte_cnt a 
    right join flights b
    on (a.flight_id = b.flight_id)
    order by b.flight_id;