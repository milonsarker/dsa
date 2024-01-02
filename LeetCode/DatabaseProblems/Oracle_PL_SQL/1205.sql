--https://leetcode.com/problems/monthly-transactions-ii/

/* Write your PL/SQL query statement below */
WITH approved_transactions as (
    SELECT id,
		   country,
		   state,
		   amount,
		   to_char(trans_date, 'YYYY-MM') as month
    FROM Transactions WHERE state='approved'
),
chargeback_transactions as (
    SELECT c.trans_id,
	       t.country,
		   'chargeback' as state,
		   t.amount,
		   to_char(c.trans_date, 'YYYY-MM') as month
	FROM Chargebacks c INNER JOIN Transactions t on c.trans_id = t.id
),
all_transactions as (
    SELECT * FROM approved_transactions
    UNION
    SELECT * FROM chargeback_transactions
) SELECT month,
        country,
        SUM(CASE WHEN state='approved' THEN 1 ELSE 0 end) as approved_count,
        SUM(CASE WHEN state='approved' THEN amount ELSE 0 end) as approved_amount,
        SUM(CASE WHEN state='chargeback' THEN 1 ELSE 0 end) as chargeback_count,
        SUM(CASE WHEN state='chargeback' THEN amount ELSE 0 end) as chargeback_amount
    FROM all_transactions GROUP BY month, country;