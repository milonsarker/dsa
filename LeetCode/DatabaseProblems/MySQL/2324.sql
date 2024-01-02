#https://leetcode.com/problems/product-sales-analysis-iv/description/


# Write your MySQL query statement below
with cte_max as
(
    select user_id, a.product_id, (sum(price * quantity)) price
        from sales a
        join product b
        on (a.product_id = b.product_id)
        group by user_id, a.product_id
)
select a.user_id, a.product_id
    from cte_max a
    join
    (select user_id , max(price) max_price
        from cte_max
        group by
        user_id) b
    on (a.user_id = b.user_id  and a.price = b.max_price)
    ;