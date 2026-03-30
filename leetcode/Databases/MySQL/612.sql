#https://leetcode.com/problems/shortest-distance-in-a-plane/description/

# Write your MySQL query statement below
select min(round(sqrt((b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)),2)) shortest
    from point2d a
    cross join
         point2d b
    on (a.x <> b.x or a.y <> b.y)