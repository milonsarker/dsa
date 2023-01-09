#https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/description/


# Write your MySQL query statement below
with cte_cm as
(
    select a.user_id user1_id, b.user_id user2_id, count(*) cnt
        from relations a
        join
             relations b
        on (a.user_id < b.user_id)
        where a.follower_id = b.follower_id
        group by 1, 2
)
select user1_id, user2_id
    from cte_cm
    where cnt = (select max(cnt) from cte_cm)
    ;