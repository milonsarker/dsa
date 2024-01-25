#https://leetcode.com/problems/count-the-number-of-experiments/description/

# Write your MySQL query statement below
with cte_p as
(
    select 'Android' pid union select 'IOS' union select 'Web'
),
cte_en as
(
    select 'Reading' enid union select  'Sports' union select  'Programming'
),
cte_fl as
(
    select *
        from cte_p
        cross join
             cte_en
)
select b.pid platform, b.enid experiment_name, ifnull(count(distinct a.experiment_id),0) num_experiments
    from experiments a
    right join
         cte_fl b
    on (a.platform = b.pid and a.experiment_name = b.enid)
    group by b.pid, b.enid