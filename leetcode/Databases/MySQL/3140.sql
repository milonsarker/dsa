#https://leetcode.com/problems/consecutive-available-seats-ii/

# Write your MySQL query statement below

with cte_free_seats as 
(
    select * , seat_id - row_number() over (order by seat_id asc) gap
        from cinema
        where free = 1
        order by seat_id
), 
cte_free_seats_rnk as 
(
    select min(seat_id) first_seat_id, max(seat_id) last_seat_id, count(*) consecutive_seats_len, 
            rank() over(order by count(*) desc) as rnk
        from cte_free_seats
        group by gap
)
select first_seat_id, last_seat_id, consecutive_seats_len 
    from cte_free_seats_rnk 
    where rnk = 1
    order by first_seat_id
    ;