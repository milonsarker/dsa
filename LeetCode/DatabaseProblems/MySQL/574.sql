#https://leetcode.com/problems/winning-candidate/description/


# Write your MySQL query statement below
with cte_cnt as
(
    select candidateid, count(*) vcnt
        from vote
        group by candidateid
),
cte_rnk as
(
    select candidateid, rank() over (order by vcnt desc) rnk
        from cte_cnt
)
select b.name
    from cte_rnk a
    join candidate b
    on (b.id = a.candidateid)
    where rnk = 1;