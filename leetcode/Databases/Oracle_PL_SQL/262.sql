--https://leetcode.com/problems/trips-and-users/

/* Write your PL/SQL query statement below */
select
    t.Request_at as Day,
    round(count(case when t.status!='completed' then t.id end) / count(*), 2) as "Cancellation Rate"
from Trips t
join Users c on t.Client_Id = c.Users_Id
join Users d on t.Driver_Id = d.Users_Id
where
    c.Banned = 'No' and
    d.Banned = 'No' and
    t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at;