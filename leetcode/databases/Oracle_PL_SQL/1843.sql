--https://leetcode.com/problems/suspicious-bank-accounts/

/* Write your PL/SQL query statement below */
with cte_credit as
(
    select account_id, substr(day, 1,7) month , sum(amount) tot_deposit
        from transactions
        where type = 'Creditor'
        group by account_id, substr(day, 1,7)
),
cte_ex_max_inc as
(
    select a.*
        from cte_credit a
        join
             accounts b
        on (a.account_id = b.account_id)
        where a.tot_deposit > b.max_income
)
select distinct account_id
    from (
            select  account_id,
                    to_date(month, 'yyyy-mm') - lag(to_date(month,'yyyy-mm'), 1, to_date(month, 'yyyy-mm')) over(partition by account_id order by to_date(month,'yyyy-mm')) as lag_month
                from cte_ex_max_inc
         )
    where lag_month in (28,30,31);