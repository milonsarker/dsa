--https://leetcode.com/problems/product-sales-analysis-ii/

/* Write your PL/SQL query statement below */
select product_id, sum(quantity) total_quantity
    from sales
    group by product_id