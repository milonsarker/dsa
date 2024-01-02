--https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/


/* Write your PL/SQL query statement below */
with cte_p_cnt as
(
    select passenger_id, count(*) cnt
        from rides
        group by passenger_id
)
select distinct b.driver_id, nvl(a.cnt, 0) cnt
    from cte_p_cnt a
    right join
         rides b
    on (a.passenger_id = b.driver_id);
