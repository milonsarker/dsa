# https://leetcode.com/problems/analyze-subscription-conversion/description/

# Write your MySQL query statement below
select  user_id, round(avg(case when activity_type = 'free_trial' then activity_duration end), 2) trial_avg_duration, 
        round(avg(case when activity_type = 'paid' then activity_duration end), 2) paid_avg_duration 
    from UserActivity
    group by user_id
    having round(avg(case when activity_type = 'paid' then activity_duration end), 2) > 0
    order by user_id;
