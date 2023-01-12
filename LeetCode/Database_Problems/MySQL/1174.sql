#https://leetcode.com/problems/immediate-food-delivery-ii/description/


# Write your MySQL query statement below
with cte_fo as
(
    select customer_id, min(order_date) odate
        from delivery
        group by customer_id
),
cte_sc as
(
    select 1 id, count(*) sc_cnt
        from delivery a
        join cte_fo b
        on (a.customer_id = b.customer_id and a.order_date = b.odate)
),
cte_im as
(
    select 1 id, count(*) cnt
        from delivery a
        join cte_fo b
        on (a.customer_id = b.customer_id and a.order_date = b.odate)
        where a.customer_pref_delivery_date = a.order_date
)
select round(b.cnt*100/a.sc_cnt, 2) immediate_percentage
    from cte_sc a
    join cte_im b
    on (a.id = b.id)