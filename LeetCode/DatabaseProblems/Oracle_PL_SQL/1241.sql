--https://leetcode.com/problems/number-of-comments-per-post/

/* Write your PL/SQL query statement below */
select a.sub_id post_id, nvl(count(b.parent_id),0) number_of_comments
    from
        (select distinct sub_id from submissions where parent_id is null) a
        left join
         (select distinct sub_id, parent_id from submissions) b
    on (a.sub_id = b.parent_id)
    group by a.sub_id
    order by 1