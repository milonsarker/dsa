#https://leetcode.com/problems/find-books-with-no-available-copies/

# Write your MySQL query statement below
with bcount as
(
    select book_id, count(*) bcount
        from borrowing_records
        where return_date is null
        group by book_id
        
)
select a.book_id, a.title, a.author, a.genre, a.publication_year, bcount current_borrowers
    from library_books a 
    join bcount b on (a.book_id = b.book_id)
    where a.total_copies = b.bcount
    order by bcount desc, a.title;

