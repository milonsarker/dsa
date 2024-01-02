--https://leetcode.com/problems/unique-orders-and-customers-per-month/

/* Write your PL/SQL query statement below */
select to_char(order_date,'yyyy-mm') month, count(distinct order_id) order_count, count(distinct customer_id) customer_count
    from orders
    where invoice > 20
    group by to_char(order_date,'yyyy-mm')