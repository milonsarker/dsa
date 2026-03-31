# https://leetcode.com/problems/customer-purchasing-behavior-analysis/
# Write your MySQL query statement below

with cte_freq_prod as 
(
    select * from 
        (
        select a.customer_id, a.CATEGORY, rank() over (partition by customer_id order by count(*) desc, max(transaction_date) desc) as rnk
            from (
                    SELECT  a.customer_id, b.category, a.transaction_date
                        FROM transactions A 
                        JOIN PRODUCTS B 
                        ON (A.PRODUCT_ID = B.PRODUCT_ID)

                ) A
            group by a.customer_id, a.CATEGORY
        ) xx
        where rnk = 1
), 
cte_base as 
(
    select A.customer_id, sum(amount) total_amount, count(transaction_id) transaction_count , count(distinct CATEGORY) unique_categories, 
            avg(amount) avg_transaction_amount, 
            round((sum(amount)/ 100 + count(transaction_id) * 10), 2) loyalty_score
        from transactions A 
        JOIN PRODUCTS B 
        ON (A.PRODUCT_ID = B.PRODUCT_ID)
        group by customer_id
)

select A.CUSTOMER_ID, A.TOTAL_AMOUNT, A.TRANSACTION_COUNT, A.UNIQUE_CATEGORIES, 
        ROUND(A.AVG_TRANSACTION_AMOUNT, 2) AVG_TRANSACTION_AMOUNT, B.CATEGORY TOP_CATEGORY, ROUND(A.LOYALTY_SCORE, 2) LOYALTY_SCORE
    from cte_base a 
    join cte_freq_prod b
    on (a.customer_id = b.customer_id)
    order by A.LOYALTY_SCORE DESC, a.customer_id
    ;