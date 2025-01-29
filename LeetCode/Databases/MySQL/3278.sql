# https://leetcode.com/problems/find-candidates-for-data-scientist-position-ii/
# Write your MySQL query statement below

with cte_skill_cnt as 
(
    select project_id, count(*) skill_cnt
        from projects
        group by project_id
), 
cte_skill_join
(
    select  b.project_id, a.candidate_id, 
            sum(case when proficiency > importance then 10 
                     when proficiency = importance then 0
                     else -5 end) + 100 as score, 
            count(*) skill_count
        from candidates a 
        right join projects b on (a.skill = b.skill)
        group by b.project_id, a.candidate_id
), 
cte_rnk as 
(
    select project_id, candidate_id, score, 
            rank() over (partition by project_id order by score desc, candidate_id) as rnk
        from cte_skill_join
        where (project_id, skill_count) in (select project_id, skill_cnt from cte_skill_cnt)
)
select project_id, candidate_id, score
    from cte_rnk
    where rnk = 1
    order by project_id;