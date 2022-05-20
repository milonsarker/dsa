--https://leetcode.com/problems/leetflex-banned-accounts/

/* Write your PL/SQL query statement below */
select distinct a.account_id
    from loginfo a
    join
         loginfo b
    on (a.account_id = b.account_id)
    where a.ip_address <> b.ip_address
    and (a.login between b.login and b.logout or b.login between a.login and a.logout)