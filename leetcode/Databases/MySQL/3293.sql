# https://leetcode.com/problems/calculate-product-final-price/
# Write your MySQL query statement below

select product_id, price - (price * ifnull(discount, 0) / 100) final_price , a.category 
    from products a 
    left join discounts b
    on (a.category = b.category) 
    order by product_id