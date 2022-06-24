--https://leetcode.com/problems/article-views-ii/

/* Write your PL/SQL query statement below */
select distinct viewer_id id
    from views
    group by viewer_id, to_char(view_date,'yyyymmdd')
    having count(distinct article_id) > 1
    order by 1;