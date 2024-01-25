#https://leetcode.com/problems/the-airport-with-the-most-traffic/description/

# Write your MySQL query statement below
with cte_rnk as
(
    select ap, rank() over(order by cnt desc) rnk
        from (
            select ap, sum(flights_count) cnt
                from (
                    select departure_airport  ap, flights_count
                        from flights
                    union all
                    select arrival_airport  ap, flights_count
                        from flights
                    ) a
                group by ap
        ) b

)
select ap airport_id
    from cte_rnk
    where rnk = 1;