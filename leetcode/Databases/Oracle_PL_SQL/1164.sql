--https://leetcode.com/problems/product-price-at-a-given-date/

/* Write your PL/SQL query statement below */

with abc as
(
    select product_id, new_price, change_date,
           dense_rank() over (partition by product_id order by change_date desc) as rnk
        from Products
        where trunc(change_date) <= to_date('2019-08-16','yyyy-mm-dd')
),

xyz as
(
    select distinct a.product_id, nvl(b.new_price, 10) as price, nvl(b.rnk, 1) rnk
        from products a
        left join
             abc b
        on (a.product_id = b.product_id)
)

select product_id, price
    from xyz
    where rnk = 1