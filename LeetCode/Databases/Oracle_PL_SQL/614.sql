--https://leetcode.com/problems/second-degree-follower/

/* Write your PL/SQL query statement below */
with cte_follower as
(
    select follower, count(*) cnt
        from follow
        group by follower
),
cte_followee as
(
    select followee, count(*) cnt
        from follow
        group by followee
)
select followee follower, b.cnt num
    from cte_follower a
    join
         cte_followee b
    on (a.follower = b.followee)
    where a.cnt >= 1 and b.cnt >= 1
    order by 1;