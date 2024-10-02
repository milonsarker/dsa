# https://leetcode.com/problems/top-percentile-fraud/
# Write your MySQL query statement below

with cte_rnk as 
(
    select policy_id, state, fraud_score, rank() over (partition by state order by fraud_score desc) as rnk
        from fraud
)
select policy_id, state, fraud_score
    from cte_rnk
    where rnk = 1
    order by state, fraud_score desc, policy_id