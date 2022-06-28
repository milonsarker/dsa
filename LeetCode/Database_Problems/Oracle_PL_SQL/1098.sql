--https://leetcode.com/problems/unpopular-books/

/* Write your PL/SQL query statement below */
with cte_relevant_books as
(
    select book_id, name
        from books
        where to_date(available_from) < add_months(to_date('2019-06-23'), -1)
),
cte_sales as
(
    select book_id, sum(quantity) sales
        from orders
        where dispatch_date between add_months(to_date('2019-06-23'), -12) and to_date('2019-06-23')
        group by book_id
)
select a.book_id, a.name
    from cte_relevant_books a
    left join
         cte_sales  b
    on (a.book_id = b.book_id)
    where nvl(b.sales,0) < 10;