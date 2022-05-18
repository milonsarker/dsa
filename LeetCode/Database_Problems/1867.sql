--https://leetcode.com/problems/orders-with-maximum-quantity-above-average/

/* Write your PL/SQL query statement below */
with cte_max_order as
(
    select order_id, max(quantity) m_quantity
        from OrdersDetails
        group by order_id
),
cte_avg_quantitiy as
(
    select order_id, sum(quantity)/count(distinct product_id) avg_quant
        from OrdersDetails
        group by order_id
)
select a.order_id
    from cte_max_order a
    where a.m_quantity > (select max(avg_quant) from cte_avg_quantitiy)