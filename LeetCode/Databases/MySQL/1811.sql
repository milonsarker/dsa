#https://leetcode.com/problems/find-interview-candidates/description/

# Write your MySQL query statement below

with cte_com as
(
    select contest_id, gold_medal id, 'g' medal
        from contests
    union all
    select contest_id, bronze_medal id, 'b' medal
        from contests
    union all
    select contest_id, silver_medal id, 's' medal
        from contests
),
cte_cons as
(
    select distinct a.id
        from cte_com a
        join
             cte_com b
        on (a.contest_id = b.contest_id + 1)
        join
             cte_com c
        on (a.contest_id = c.contest_id - 1)
        where a.id = b.id
        and a.id =c.id
),
cte_gm as
(
    select gold_medal gmid
        from contests
        group by 1
        having count(*)>=3
)
select c.name, c.mail
    from (select * from cte_cons
            union
          select * from cte_gm
         ) a
    join
         users c
    on(a.id = c.user_id);