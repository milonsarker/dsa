--https://leetcode.com/problems/calculate-orders-within-each-interval/

select case when minute % 6 <> 0 then floor((minute / 6) + 1) 
            else minute/6 end interval_no, sum(order_count) total_orders
    from orders
    group by 1 
    order by 1;