/* Write your PL/SQL query statement below */
select case
            when mod(id, 2) = 0 then id - 1
            when id = (select max(id) from seat) then id
            else id + 1
        end id,
        student
    from seat
    order by 1