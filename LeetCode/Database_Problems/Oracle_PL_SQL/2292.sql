--https://leetcode.com/problems/products-with-three-or-more-orders-in-two-consecutive-years/

/* Write your PL/SQL query statement below */
with cte_prod as
(
    select product_id, to_char(purchase_date,'yyyy') p_year , count(*) cnt
        from orders
        group by product_id, to_char(purchase_date,'yyyy')
        having count(*) >= 3
)
select distinct product_id
    from (
            select product_id, p_year , lag(p_year, 1) over(partition by product_id order by p_year) l_year
                from cte_prod
         )
    where p_year - l_year = 1;