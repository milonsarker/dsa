--https://leetcode.com/problems/rectangles-area/

/* Write your PL/SQL query statement below */
select p1.id p1, p2.id p2,
       abs(p1.x_value - p2.x_value) * abs(p1.y_value - p2.y_value) area
    from points p1
    inner join
         points p2
    on (
            p1.id < p2.id and
            p1.x_value <> p2.x_value and
            p1.y_value <> p2.y_value
       )
    order by 1 desc , 2, 3
