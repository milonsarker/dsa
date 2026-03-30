--https://leetcode.com/problems/products-price-for-each-store/
/* Write your PL/SQL query statement below */
select *
    from products
    pivot
    (
        max(price) for store in ('store1' as store1, 'store2' as store2, 'store3' as store3)
    )