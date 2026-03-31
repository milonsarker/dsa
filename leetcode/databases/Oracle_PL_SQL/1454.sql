--https://leetcode.com/problems/active-users/

/* Write your PL/SQL query statement below */
with cte_login_lag as
(
    select id, login_date,
           lag(login_date, 4) over(partition by id order by login_date) as lagged
        from (select distinct id, login_date from logins)
)
select distinct a.id, b.name
    from cte_login_lag a
    join
         accounts b
    on (a.id = b.id)
    where (login_date - lagged) = 4
    order by a.id;