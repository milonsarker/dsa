#https://leetcode.com/problems/friday-purchases-ii/
with recursive date_range as 
(
    select date('2023-11-01') as dt
    union all
    select dt + interval 1 day
        from date_range
        where dt < date('2023-11-30')
), 
cte_join as 
(
    select a.dt purchase_date, ifnull(sum(amount_spend),0) total_amount
        from date_range a 
        left join purchases b
        on (a.dt = b.purchase_date)
        where dayofweek(dt) = 6
        group by a.dt
)
select rank() over(order by purchase_date ) week_of_month,  a.* 
    from cte_join a;