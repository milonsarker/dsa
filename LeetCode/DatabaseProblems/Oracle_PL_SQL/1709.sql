--https://leetcode.com/problems/biggest-window-between-visits/

/* Write your PL/SQL query statement below */
with cte_window as
(
    select user_id, visit_date,
           lead(visit_date, 1) over(partition by user_id order by visit_date) next_visit_date
        from uservisits
)
select  user_id, max(nvl(next_visit_date, to_date('2021-01-01','yyyy-mm-dd')) - visit_date) biggest_window
    from cte_window
    group by user_id
    order by user_id;