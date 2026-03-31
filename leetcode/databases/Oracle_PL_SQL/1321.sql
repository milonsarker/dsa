--https://leetcode.com/problems/restaurant-growth/

/* Write your PL/SQL query statement below */
with date_wise_amt as
(
    select to_char(visited_on, 'yyyy-mm-dd') visited_on, sum(amount) amount
        from customer
        group by to_char(visited_on, 'yyyy-mm-dd')
),
windowing_data as
(
    select visited_on,
           sum(amount) over (order by visited_on rows between 6 preceding and current row) amount,
           avg(amount) over (order by visited_on rows between 6 preceding and current row) average_amount,
           row_number() over (order by visited_on asc) as sw_rnk
        from date_wise_amt
)
select visited_on, amount, round(average_amount, 2) average_amount
    from windowing_data
    where sw_rnk >= 7
    order by visited_on