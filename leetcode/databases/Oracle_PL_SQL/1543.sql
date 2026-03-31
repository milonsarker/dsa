--https://leetcode.com/problems/fix-product-name-format/

/* Write your PL/SQL query statement below */
select lower(trim(product_name)) product_name, to_char(sale_date,'yyyy-mm') sale_date, count(sale_id) total
    from sales
    group by lower(trim(product_name)) , to_char(sale_date,'yyyy-mm')
    order by 1 ,2 ;