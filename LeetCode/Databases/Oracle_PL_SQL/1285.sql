--https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/

/* Write your PL/SQL query statement below */
with cte_cons_groups as
(
    select log_id, log_id  - rank() over (order by log_id) grp
        from logs
)
select min(log_id) start_id, max(log_id) end_id
    from cte_cons_groups
    group by grp
    order by 1 ;