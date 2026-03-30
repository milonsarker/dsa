--https://leetcode.com/problems/confirmation-rate/

/* Write your PL/SQL query statement below */
with cte_conf_timeout as
(
    select user_id,
           sum( case
                    when action = 'confirmed' then 1  else 0
                end
              ) conf,
           count(*) total
        from confirmations
        group by user_id
)
select b.user_id, round(nvl(conf,0)/nvl(total,1), 2) confirmation_rate
    from cte_conf_timeout a
    right join
         signups b
    on (a.user_id = b.user_id);