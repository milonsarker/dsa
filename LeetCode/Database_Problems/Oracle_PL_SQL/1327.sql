--https://leetcode.com/problems/list-the-products-ordered-in-a-period/

/* Write your PL/SQL query statement below */
with cte_tot_unit as
(
    select product_id, sum(unit) tot_unit
        from orders
        where to_char(order_date,'yyyy-mm') = '2020-02'
        group by product_id
        having sum(unit) >= 100
)
select b.product_name, tot_unit unit
    from cte_tot_unit a
    join
         products b
    on (a.product_id = b.product_id);