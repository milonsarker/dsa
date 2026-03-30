--https://leetcode.com/problems/customers-who-bought-all-products/

/* Write your PL/SQL query statement below */
with tot_prod_cnt as
(
    select customer_id, count(distinct product_key) cnt
        from customer
        group by customer_id
)
select customer_id
    from tot_prod_cnt
    where cnt = (select count(*) from product)