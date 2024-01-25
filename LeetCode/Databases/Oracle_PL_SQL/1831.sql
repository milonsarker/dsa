--https://leetcode.com/problems/maximum-transaction-each-day/

/* Write your PL/SQL query statement below */
with cte_max_amt as
(
    select to_char(day,'yyyy-mm-dd') day, max(amount) amt
        from Transactions
        group by to_char(day,'yyyy-mm-dd')
)

select distinct transaction_id
    from Transactions a
    join
         cte_max_amt b
    on (a.amount = b.amt and to_char(a.day,'yyyy-mm-dd') = b.day)
    order by 1;