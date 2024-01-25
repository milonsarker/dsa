--https://leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list/

select artist, count(*) occurrences
    from spotify
    group by artist
    order by 2 desc, 1;