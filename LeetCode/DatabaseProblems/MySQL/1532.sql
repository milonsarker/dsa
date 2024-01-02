#https://leetcode.com/problems/the-most-recent-three-orders/description/


# Write your MySQL query statement below
with cte_rnk as
(
    select a.*, rank() over (partition by customer_id order by order_date desc) rnk
        from orders a
)
select b.name customer_name, a.customer_id, a.order_id, a.order_date
    from cte_rnk a
    join customers b
    on (a.customer_id = b.customer_id)
    where a.rnk <= 3
    order by customer_name, customer_id, order_date desc;