#https://leetcode.com/problems/the-category-of-each-member-in-the-store/description/


# Write your MySQL query statement below

with cte_visits as
(
    select member_id, count(*) v_cnt
        from visits
        group by member_id
),
cte_purc as
(
    select a.member_id, count(*) p_cnt
        from visits a
        join purchases b
        on (a.visit_id = b.visit_id)
        group by a.member_id
)
select c.member_id, c.name,
    case when b.v_cnt is null then 'Bronze'
         when  (100 * ifnull(a.p_cnt, 0)) / ifnull(b.v_cnt,1) >= 80 then 'Diamond'
         when  (100 * ifnull(a.p_cnt, 0))  / ifnull(b.v_cnt,1) >= 50 and (100 * ifnull(a.p_cnt, 0))  / ifnull(b.v_cnt,1) < 80 then 'Gold'
         when  (100 * ifnull(a.p_cnt, 0))  / ifnull(b.v_cnt,1) < 50 then 'Silver'
    end category
    from cte_purc a
    right join
         cte_visits b
    on (a.member_id = b.member_id)
    right join
         members c
    on (c.member_id = b.member_id);