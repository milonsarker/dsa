--https://leetcode.com/problems/the-winner-university/

/* Write your PL/SQL query statement below */
with cte_nyc as
(
    select count(*) cnt_nyc, 2 dummy
        from newyork
        where score >= 90
),
cte_cf as
(
    select count(*) cnt_cf, 2 dummy
        from California
        where score >= 90
)
select case
            when cnt_nyc > cnt_cf
                then 'New York University'
            when cnt_nyc < cnt_cf
                then 'California University'
            else 'No Winner'
        end winner
    from cte_nyc a
    join
         cte_cf b
    on (a.dummy = b.dummy)