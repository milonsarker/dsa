--https://leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/

/* Write your PL/SQL query statement below */
with cte_rnk as
(
    select city_id, to_char(day,'yyyy-mm-dd') day, degree,
           rank() over(partition by city_id order by degree desc, day) as rnk
        from weather
)
select city_id, day, degree
    from cte_rnk
    where rnk = 1
    order by city_id;