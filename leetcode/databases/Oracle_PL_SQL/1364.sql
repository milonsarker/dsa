--https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/

/* Write your PL/SQL query statement below */
with cte_contacts as
(
    select user_id , count(*)  contacts_cnt ,
        sum(case
                when contact_email in (select email from customers) then 1
                else 0
            end) trusted_contacts_cnt
        from contacts
        group by user_id
)
select b.invoice_id, c.customer_name, b.price,
       nvl(a.contacts_cnt, 0) contacts_cnt,
       nvl(a.trusted_contacts_cnt,0) trusted_contacts_cnt
    from cte_contacts a
    right join
         Invoices b
    on (a.user_id = b.user_id)
     join
         Customers c
    on (b.user_id = c.customer_id)
    order by 1;