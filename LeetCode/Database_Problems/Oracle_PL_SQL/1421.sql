--https://leetcode.com/problems/npv-queries/

/* Write your PL/SQL query statement below */
select b.id, b.year, nvl(a.npv, 0) npv
    from npv a
    right join
         queries b
    on (a.id = b.id and a.year = b.year)