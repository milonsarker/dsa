--https://leetcode.com/problems/ads-performance/

/* Write your PL/SQL query statement below */
with cte_ad_summ as
(
    select ad_id,
         sum(case
                when action = 'Clicked' then 1
                else 0
            end) tot_clicked,
         sum(case
                when action = 'Viewed' then 1
                else 0
            end) tot_viewed
        from ads
        group by ad_id
)
select ad_id,
        case
            when tot_clicked + tot_viewed = 0 then 0
            else round((tot_clicked) * 100 /(tot_clicked + tot_viewed) , 2)
        end ctr
    from cte_ad_summ
    order by ctr desc , ad_id asc;