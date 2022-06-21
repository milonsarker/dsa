--https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/

/* Write your PL/SQL query statement below */
with cte_cust_zero as
(
    select distinct customer_id
        from orders
        where order_type = 0
)
select *
    from orders
    where customer_id not in (select customer_id from cte_cust_zero)
union all
select *
    from orders
    where order_type = 0 and customer_id in (select customer_id from cte_cust_zero);