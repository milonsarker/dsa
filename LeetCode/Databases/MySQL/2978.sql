#https://leetcode.com/problems/symmetric-coordinates/
with cte_rn as 
(
    select *, row_number() over () as rn
        from coordinates
)
select  distinct a.x, a.y
    from cte_rn a 
    inner join cte_rn b
    on (a.x = b.y and a.y = b.x and a.rn <> b.rn)
    where a.x <= a.y
    order by a.x, a.y;