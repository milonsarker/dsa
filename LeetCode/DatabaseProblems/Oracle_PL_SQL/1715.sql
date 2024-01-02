--https://leetcode.com/problems/count-apples-and-oranges/

/* Write your PL/SQL query statement below */
select sum(a.apple_count + nvl(b.apple_count,0)) apple_count ,
       sum(a.orange_count + nvl(b.orange_count,0)) orange_count
    from boxes a
    left join
         chests b
    on (a.chest_id = b.chest_id);