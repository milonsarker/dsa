--https://leetcode.com/problems/immediate-food-delivery-iii/

select order_date, 
    round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) * 100 /count(*), 2) immediate_percentage
    from delivery
    group by order_date
    order by 1