--https://leetcode.com/problems/evaluate-boolean-expression/

/* Write your PL/SQL query statement below */
with abc as
(
    select a.*, (select value from variables where name = a.left_operand) xval, (select value from variables where name = a.right_operand) yval
        from expressions a
)
select left_operand, operator, right_operand,
        case
            when operator = '>' then (case when xval > yval then 'true' else 'false' end)
            when operator = '<' then (case when xval < yval then 'true' else 'false' end)
            when operator = '=' then (case when xval = yval then 'true' else 'false' end)
            else 'false'
        end value
    from abc