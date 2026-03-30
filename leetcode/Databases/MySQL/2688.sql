# https://leetcode.com/problems/find-active-users/
with cte_lead as
(
    select user_id, created_at first_buy, lead(created_at) over (partition by user_id order by created_at) second_buy
        from users
)
select distinct user_id
    from cte_lead
    
    where second_buy between first_buy and date_add(first_buy, interval 7 day);