# https://leetcode.com/problems/find-trending-hashtags/
# Write your MySQL query statement below

select regexp_substr(tweet, '\#[a-zA-Z]+') hashtag, count(*) hashtag_count
    from tweets
    group by regexp_substr(tweet, '\#[a-zA-Z]+')
    order by hashtag_count desc, hashtag desc
    limit 3
    ; 