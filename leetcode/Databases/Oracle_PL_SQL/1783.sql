--https://leetcode.com/problems/grand-slam-titles/

with abc as
(
    select *
        from Championships
        unpivot
        (pid for gst in  (Wimbledon, Fr_open  , US_open  , Au_open))
)
select b.player_id, b.player_name, count(a.pid) grand_slams_count
    from abc a
    join
         players  b
    on (a.pid = b.player_id)
    group by b.player_id, b.player_name;


/* Write your PL/SQL query statement below */
select b.player_id player_id, b.player_name, count(id) grand_slams_count
    from
        (
            select year, wimbledon id from Championships
            union all
            select year, Fr_open  id from Championships
            union all
            select year, US_open id from Championships
            union all
            select year, Au_open id  from Championships
        ) a,
        players b
        where a.id = b.player_id
        group by b.player_id , b.player_name
        ;