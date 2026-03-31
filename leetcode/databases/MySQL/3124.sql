# https://leetcode.com/problems/find-longest-calls/

# Write your MySQL query statement below

with cte_rnk as 
(
    select a.first_name, b.type, b.duration,  rank() over (partition by b.type order by duration desc) as rnk
        from contacts a 
        join calls b
        on (a.id = b.contact_id)
)
select first_name, type, CONCAT_WS(':', LPAD(CONVERT(duration DIV 3600, char), 2, '0'),
                                    LPAD(CONVERT(MOD(duration, 3600) DIV 60 , char), 2, '0'),
                                    LPAD(CONVERT(MOD(duration, 60), char), 2, '0')
                                    ) AS duration_formatted
    from cte_rnk
    where rnk <= 3
    order by type desc, rnk, first_name desc;