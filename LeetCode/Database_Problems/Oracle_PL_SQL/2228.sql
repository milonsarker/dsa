--https://leetcode.com/problems/users-with-two-purchases-within-seven-days/

/* Write your PL/SQL query statement below */
with cte_lag as
(
    select user_id,
           purchase_date - lag(purchase_date) over(partition by user_id order by purchase_date) as ldate
        from purchases
)
select distinct user_id
    from cte_lag
    where ldate <= 7;