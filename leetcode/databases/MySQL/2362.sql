#https://leetcode.com/problems/generate-the-invoice/description/


# Write your MySQL query statement below
with cte_tot as
(
    select b.product_id, b.invoice_id, b.quantity, b.quantity * a.price price
        from products a
        join
             purchases b
        on (a.product_id = b.product_id)
),
cte_top as
(
    select a.*, rank() over(order by tot_price desc, invoice_id asc) rnk
        from (select invoice_id , sum(price) tot_price from cte_tot group by invoice_id) a
)
select b.product_id, b.quantity, b.price
    from cte_top a
    join
         cte_tot b
    on (a.invoice_id = b.invoice_id)
    where a.rnk = 1
    ;