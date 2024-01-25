#https://leetcode.com/problems/find-the-missing-ids/description/

# Write your MySQL query statement below
with recursive ids as
(
    select 1 as id
    union
    select id + 1
        from ids
        where id < (select max(customer_id) from customers)
)
select id ids
    from ids
    where id not in (select customer_id from customers);