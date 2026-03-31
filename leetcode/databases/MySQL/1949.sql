#https://leetcode.com/problems/strong-friendship/description/



# Write your MySQL query statement below
with cte_frnd as
(
    select user1_id friend, user2_id friend_with
        from friendship
    union
    select user2_id friend, user1_id friend_with
        from friendship
)
select user1_id, user2_id , count(*) common_friend
    from friendship a
    join
         cte_frnd b
    on (a.user1_id = b.friend)
    join
         cte_frnd c
    on (a.user2_id = c.friend and b.friend_with = c.friend_with)
    group by user1_id, user2_id
    having count(*) >= 3
    ;