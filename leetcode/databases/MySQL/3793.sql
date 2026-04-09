#https://leetcode.com/problems/find-users-with-high-token-usage/description/

# Write your MySQL query statement below

with base as 
(
    select user_id, count(*) prompt_count, round(avg(tokens), 2) avg_tokens
        from prompts 
        group by user_id 
        having count(*) > 2
)
select distinct a.* 
    from base a 
    join prompts b on (a.user_id = b.user_id)
    where b.tokens > a.avg_tokens
    order by avg_tokens desc, user_id
    ;

