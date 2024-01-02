--https://leetcode.com/problems/product-sales-analysis-i/

/* Write your PL/SQL query statement below */
select b.product_name, a.year, a.price
    from sales a
    join
         product b
    on (a.product_id = b.product_id)