--https://leetcode.com/problems/products-worth-over-invoices/

/* Write your PL/SQL query statement below */
with cte_summ as
(
    select product_id, sum(rest) rest, sum(paid) paid, sum(canceled) canceled, sum(refunded) refunded
        from invoice
        group by product_id
)
select a.name, nvl(rest, 0) rest, nvl(paid,0) paid, nvl(canceled,0) canceled, nvl(refunded,0) refunded
    from product a
        left join
         cte_summ b
    on (a.product_id = b.product_id)
    order by 1