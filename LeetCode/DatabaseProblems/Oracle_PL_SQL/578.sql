--https://leetcode.com/problems/get-highest-answer-rate-question/

/* Write your PL/SQL query statement below */
with cte_qid as
(
    select question_id,
           sum(case
                    when action = 'answer' then 1 else 0
               end
              )  /
           sum(case
                    when action = 'show' then 1 else 0
               end
              ) ans_rate
        from surveylog
        group by question_id
)
select question_id survey_log
    from (
            select question_id, ans_rate, dense_rank() over(order by ans_rate desc, question_id) as rnk
                from cte_qid
         )
    where rnk = 1;