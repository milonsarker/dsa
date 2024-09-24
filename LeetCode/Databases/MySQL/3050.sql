# https://leetcode.com/problems/pizza-toppings-cost-analysis/

# Write your MySQL query statement below

select  concat(a.topping_name,',', b.topping_name,',', c.topping_name) pizza, 
        (a.cost + b.cost + c.cost) total_cost
    from toppings a 
    join toppings b
    on (a.topping_name < b.topping_name)
    join toppings c
    on (b.topping_name < c.topping_name)
    order by total_cost desc, pizza asc
    ;