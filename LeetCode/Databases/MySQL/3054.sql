# https://leetcode.com/problems/binary-tree-nodes/

# Write your MySQL query statement below

select  n, 
        case
            when p is null then 'Root' 
            when n in (select p from tree) then 'Inner' 
            else 'Leaf'
        end Type
    from tree 
    order by n
    ;