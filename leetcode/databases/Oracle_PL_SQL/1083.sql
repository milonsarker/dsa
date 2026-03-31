--https://leetcode.com/problems/sales-analysis-ii/

/* Write your PL/SQL query statement below */
with cte_s8 as
(
    select buyer_id
        from product a
        join
             sales b
        on (a.product_id = b.product_id)
        where a.product_name = 'S8'
),
cte_apple as
(
    select buyer_id
        from product a
        join
             sales b
        on (a.product_id = b.product_id)
        where a.product_name = 'iPhone'
)
select *
    from cte_s8
minus
select *
    from cte_apple;