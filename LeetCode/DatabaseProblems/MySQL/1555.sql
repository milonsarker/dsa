#https://leetcode.com/problems/bank-account-summary/description/

# Write your MySQL query statement below
with cte_un as
(
    select uid, sum(a.amount) credit
        from (
                select paid_by uid, -amount amount
                    from Transactions
                union all
                select paid_to uid, amount
                    from Transactions
              ) a
        group by uid
)
select a.user_id, a.user_name, ifnull(b.credit, 0) + a.credit credit,
        case when ifnull(b.credit, 0) + a.credit < 0 then 'Yes' else 'No' end credit_limit_breached
    from users a
    left join
         cte_un b
    on (a.user_id = b.uid)