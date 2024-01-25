--https://leetcode.com/problems/convert-date-format/

/* Write your PL/SQL query statement below */
select TO_CHAR(DAY,'FMDay')||', '||to_char(day, 'FMMonth DD, YYYY') DAY
    from days;