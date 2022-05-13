--https://leetcode.com/problems/countries-you-can-safely-invest-in/

SELECT
 co.name AS country
FROM
 person p
 JOIN
     country co
     ON SUBSTR(phone_number,1,3) = country_code
 JOIN
     calls c
     ON p.id IN (c.caller_id, c.callee_id)
GROUP BY
 co.name
HAVING
 AVG(duration) > (SELECT AVG(duration) FROM calls)