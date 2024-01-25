#https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/description/

# Write your MySQL query statement below
with cte_nej as
(
    select a.bus_id, a.arrival_time btime, b.passenger_id pid, b.arrival_time ptime
    from buses a
        join
            passengers b
        on (b.arrival_time <= a.arrival_time)
),
cte_rnk as
(
    select * , rank() over(partition by pid order by btime asc) rnk
        from cte_nej
)
select b.bus_id, ifnull(count(distinct pid),0) passengers_cnt
    from (select * from cte_rnk where rnk = 1) a
    right join
         buses b
    on (a.bus_id = b.bus_id)
    group by b.bus_id;