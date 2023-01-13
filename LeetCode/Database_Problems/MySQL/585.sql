#https://leetcode.com/problems/investments-in-2016/description/

# Write your MySQL query statement below
with cte_dup_ll as
(
    select lat, lon
        from insurance
        group by 1,2
        having count(*) > 1
),
cte_uniq as
(select tiv_2015
    from insurance
    group by 1
    having count(*)  = 1
)
select round(sum(tiv_2016),2) tiv_2016
    from insurance
    where tiv_2015 not in (select tiv_2015 from cte_uniq) and concat(lat, lon) not in (select concat(lat,lon) from cte_dup_ll)