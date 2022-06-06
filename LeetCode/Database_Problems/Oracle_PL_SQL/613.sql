--https://leetcode.com/problems/shortest-distance-in-a-line/

/* Write your PL/SQL query statement below */
select min(abs(a.x - b.x)) shortest
    from point a
    join
        point b
    on (a.x <> b.x)