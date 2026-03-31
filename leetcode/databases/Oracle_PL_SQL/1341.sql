--https://leetcode.com/problems/movie-rating/

/* Write your PL/SQL query statement below */
With CTE_rating as
(
    Select A.user_id, B.name ,count(movie_id) cnt
        from MovieRating A
            inner join
             users B
        on (A.user_id = B.user_id)
        group by A.user_id, B.name
        order by 3 desc, 2
),

CTE_movie_rating AS
(
    select A.movie_id, B.title, avg(rating) avg_rating
        from  MovieRating A
            inner join
              movies B
        on (A.movie_id  = B.movie_id)
        where to_char(A.created_at,'YYYY-MM') = '2020-02'
        group by A.movie_id, B.title
        order by 3 desc, 2
)

select name as results
    from CTE_rating where rownum = 1
union
select title
    from CTE_movie_rating where rownum = 1;
