--https://leetcode.com/problems/sales-analysis-i/

/* Write your PL/SQL query statement below */
with cte_tot_rev as
(
    select seller_id, sum(price) rev
        from sales
        group by seller_id
)

select seller_id
    from cte_tot_rev
    where rev in (select max(rev) from cte_tot_rev)