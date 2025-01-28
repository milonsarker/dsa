# https://leetcode.com/problems/friday-purchase-iii/

# Write your MySQL query statement below

with cte_mem_comb as 
(
    select * from 
        (
            select 'Premium' as membership 
            union all 
            select 'VIP'
        ) as ty 
        cross join 
        (
            select 1 as week_of_month 
            union all 
            select 2
            union all
            select 3
            union all 
            select 4
        ) as weeks

), 
cte_amt as 
(
    select WEEK(purchase_date, 5) - WEEK(DATE_SUB(purchase_date, INTERVAL DAYOFMONTH(purchase_date) - 1 DAY), 5) + 1 AS week_of_month, 
        b.membership, 
        sum(case when DAYOFWEEK(purchase_date) = 6 then amount_spend else 0 end) total_amount
        from purchases a 
        join users b on (a.user_id = b.user_id)
        where b.membership in ('Premium', 'VIP')
        group by WEEK(purchase_date, 5) - WEEK(DATE_SUB(purchase_date, INTERVAL DAYOFMONTH(purchase_date) - 1 DAY), 5) + 1 , 
            b.membership
)
select a.week_of_month, a.membership, ifnull(b.total_amount, 0) total_amount
    from cte_mem_comb a 
    left join cte_amt b 
    on (a.week_of_month = b.week_of_month and a.membership = b.membership)
    order by 1, 2;