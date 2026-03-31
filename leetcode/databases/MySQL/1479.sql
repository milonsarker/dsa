#https://leetcode.com/problems/sales-by-day-of-the-week/
with base as 
(
    select b.item_category CATEGORY, order_date, quantity 
        from orders a 
        right join items b
        on (a.item_id = b.item_id)
)
select CATEGORY,  
        IFNULL(SUM(case when dayofweek(order_date) = 2 THEN QUANTITY end),0) MONDAY,
        IFNULL(SUM(case when dayofweek(order_date) = 3 THEN QUANTITY end),0) TUESDAY,
        IFNULL(SUM(case when dayofweek(order_date) = 4 THEN QUANTITY end),0) WEDNESDAY,
        IFNULL(SUM(case when dayofweek(order_date) = 5 THEN QUANTITY end),0) THURSDAY,
        IFNULL(SUM(case when dayofweek(order_date) = 6 THEN QUANTITY end),0) FRIDAY,
        IFNULL(SUM(case when dayofweek(order_date) = 7 THEN QUANTITY end),0) SATURDAY,
        IFNULL(SUM(case when dayofweek(order_date) = 1 THEN QUANTITY end),0) SUNDAY
    from base
    group by category
    order by category;