--https://leetcode.com/problems/arrange-table-by-gender/

/* Write your PL/SQL query statement below */
with cte_gen as
(
    select user_id, gender,
           rank() over(partition by gender order by user_id) rnk,
           case
                when gender = 'female' then 1
                when gender = 'other' then 2
                else 3
            end gen
        from genders
)
select user_id, gender
    from cte_gen
    order by rnk , gen;