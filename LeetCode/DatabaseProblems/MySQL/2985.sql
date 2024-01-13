--https://leetcode.com/problems/calculate-compressed-mean/description/

select round(sum(item_count * order_occurrences)/sum(order_occurrences), 2) average_items_per_order
    from orders;