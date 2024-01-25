#https://leetcode.com/problems/order-two-columns-independently/description/


# Write your MySQL query statement below
select first_col, second_col
    from
    (
        select first_col, row_number() over(order by first_col asc) rn
            from data
    ) a
    join
    (
        select second_col, row_number() over(order by second_col desc) rn
            from data
    ) b
    on (a.rn = b.rn)