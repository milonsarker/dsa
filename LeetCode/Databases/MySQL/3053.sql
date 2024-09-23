# https://leetcode.com/problems/classifying-triangles-by-lengths/
# Write your MySQL query statement below
select case 
            when a + b <= c or a + c <= b or b + c <= a then 'Not A Triangle'
            when a = b and a = c and b = c then 'Equilateral'
            when a = b or a = c or b = c then 'Isosceles'
            when a <> b and a <> c and b <> c then 'Scalene'
        end triangle_type
    from triangles
    ;