#https://leetcode.com/problems/market-analysis-iii/

with cte_join as 
(
    select seller_id, count(distinct item_id) cnt
    from (
        select a.order_id, a.seller_id, b.item_id, b.item_brand, c.favorite_brand
            from orders a 
            join items b on (a.item_id = b.item_id)
            join users c on (a.seller_id = c.seller_id)
    ) a
    where item_brand <> favorite_brand
    group by 1
), 
cte_rnk as
(
    select *, dense_rank() over(order by cnt desc) as rnk
        from cte_join
)
select seller_id, cnt num_items
    from cte_rnk
    where rnk = 1
    order by seller_id;
