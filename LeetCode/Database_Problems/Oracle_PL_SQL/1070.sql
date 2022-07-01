--https://leetcode.com/problems/product-sales-analysis-iii/

/* Write your PL/SQL query statement below */
with cte_year_prod as
(
    select product_id, min(year) first_year
        from sales
        group by product_id
)
select a.product_id, a.year first_year, quantity, price
    from sales a
    join
         cte_year_prod b
    on (a.product_id = b.product_id and a.year = b.first_year);