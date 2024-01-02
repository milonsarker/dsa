--https://leetcode.com/problems/the-number-of-rich-customers/

/* Write your PL/SQL query statement below */
select count(distinct customer_id) rich_count
    from store
    where amount > 500
    ;