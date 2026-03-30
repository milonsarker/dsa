#https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/

# Write your MySQL query statement below
with cte_union as
(
    select id, count(*) num
        from (
            select accepter_id id ,requester_id  friendwith
                from RequestAccepted
            union all
            select requester_id id ,accepter_id  friendwith
                from RequestAccepted
            ) a
        group by id
)
select *
    from cte_union
    where num = (select max(num) from cte_union);