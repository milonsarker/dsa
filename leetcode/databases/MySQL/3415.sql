#https://leetcode.com/problems/find-products-with-three-consecutive-digits/

# Write your MySQL query statement below
select * 
    from products 
    where name regexp '[0-9]{3}' and name not regexp '[0-9]{4,}'
    ;