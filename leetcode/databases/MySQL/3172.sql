#https://leetcode.com/problems/second-day-verification/

# Write your MySQL query statement below

select  user_id
    from emails a 
    join texts b 
    on (a.email_id = b.email_id and date(a.signup_date) = date(b.action_date) - 1)
    where b.signup_action = 'Verified'
    order by user_id