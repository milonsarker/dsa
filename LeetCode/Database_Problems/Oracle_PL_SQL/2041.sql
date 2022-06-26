--https://leetcode.com/problems/accepted-candidates-from-the-interviews/

/* Write your PL/SQL query statement below */
with cte_score as
(
    select interview_id , sum(score) score
        from rounds
        group by interview_id
)
select b.candidate_id
    from cte_score a
    join
         candidates b
    on (a.interview_id = b.interview_id)
    where b.years_of_exp >= 2
          and score > 15;