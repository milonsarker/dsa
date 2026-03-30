# https://leetcode.com/problems/friday-purchases-i/
with cte_fri as 
(
    select purchase_date, sum(amount_spend) total_amount 
        FROM PURCHASES
        where (purchase_date between '2023-11-01' and '2023-11-30') and dayofweek(purchase_date) = 6
        group by purchase_date
)
select week(purchase_date) - week('2023-11-1') + 1 as week_of_month, purchase_date, total_amount
    from cte_fri
    order by 1;