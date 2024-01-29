#https://leetcode.com/problems/find-third-transaction/
with cte_win as 
(
    select  user_id, 
            spend,
            transaction_date, 
            rank() over(partition by user_id order by transaction_date ) rnk, 
            lag(spend) over(partition by user_id order by transaction_date) sec_trxn,
            lag(spend, 2) over(partition by user_id order by transaction_date) first_trxn
        from transactions
)
select user_id, spend third_transaction_spend, transaction_date third_transaction_date 
    from cte_win
    where sec_trxn < spend and first_trxn < spend and rnk = 3;