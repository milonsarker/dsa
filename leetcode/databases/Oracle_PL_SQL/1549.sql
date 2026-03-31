--https://leetcode.com/problems/the-most-recent-orders-for-each-product/

/* Write your PL/SQL query statement below */
with recent_prod as
(
    select product_id, order_id, order_date, dense_rank() over (partition by product_id order by order_date desc) as rnk
        from orders
        order by product_id, order_id
)
select b.product_name, a.product_id, a.order_id, to_char(a.order_date, 'yyyy-mm-dd') as order_date
    from recent_prod a
    join
         products b
    on (a.product_id = b.product_id)
    where a.rnk = 1
    order by b.product_name , a.product_id, a.order_id
