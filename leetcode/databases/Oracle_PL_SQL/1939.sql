--https://leetcode.com/problems/users-that-actively-request-confirmation-messages/


/* Write your PL/SQL query statement below */
select distinct user_id from
(
    select user_id,time_stamp -lag(time_stamp) over(partition by user_id order by time_stamp) diff
        from Confirmations
)
where diff <=1;