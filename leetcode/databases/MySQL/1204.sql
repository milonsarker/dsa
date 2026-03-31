#https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/

# Write your MySQL query statement below
with cte_running as
(
    select turn, person_id, person_name,  sum(weight) over(order by turn ) running_weight
        from queue
)
select person_name
    from cte_running
    where running_weight = (select max(running_weight) from cte_running where running_weight <=1000)
