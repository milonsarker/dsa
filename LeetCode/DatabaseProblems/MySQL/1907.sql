#https://leetcode.com/problems/count-salary-categories/description/

# Write your MySQL query statement below
with cte_cat as
(
    select account_id,
           case when income < 20000 then 'Low Salary'
                when income between 20000 and 50000 then 'Average Salary'
                when income > 50000 then 'High Salary'
           end category
        from accounts
)
select b.cat category, ifnull(count(a.account_id), 0) accounts_count
    from cte_cat a
    right join
        (select 'Low Salary' cat union select 'Average Salary' cat union select 'High Salary') b
    on (a.category = b.cat)
    group by b.cat;