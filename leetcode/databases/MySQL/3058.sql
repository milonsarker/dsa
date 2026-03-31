# https://leetcode.com/problems/friends-with-no-mutual-friends/

# Write your MySQL query statement below

with all_pairs as 
(
    select  user_id1 user_id, 
            user_id2 friend
        from friends
    union all
    select  user_id2 user_id, 
            user_id1 friend
        from friends
), 
shared_friend_pairs as
(
    select  a.user_id user_id1,
            b.user_id user_id2
        from all_pairs a
        join all_pairs b
        on (a.friend = b.friend)
)
select user_id1, user_id2
    from friends 
    where (user_id1, user_id2) not in (select user_id1, user_id2 from shared_friend_pairs)
    order by user_id1, user_id2
    ;