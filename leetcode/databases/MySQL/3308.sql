# https://leetcode.com/problems/find-top-performing-driver/

# Write your MySQL query statement below

with cte_base as 
(
    select b.fuel_type, a.driver_id, avg(c.rating) rating, sum(c.distance) distance, min(a.accidents) accidents
        from drivers a 
        join vehicles b
        on (a.driver_id = b.driver_id)
        join trips c
        on (b.vehicle_id = c.vehicle_id)
        group by b.fuel_type, a.driver_id
), 
cte_rank as 
(
    select fuel_type, driver_id, rating, distance, rank() over (partition by fuel_type order by rating desc, distance desc, accidents asc) as rnk
        from cte_base
)
select fuel_type, driver_id, round(rating, 2) rating, distance
    from cte_rank
    where rnk = 1
    order by fuel_type
    ;