#https://leetcode.com/problems/number-of-accounts-that-did-not-stream/description/


# Write your MySQL query statement below
select count(*) accounts_count
    from subscriptions
    where '2021'  in (year(start_date), year(end_date))
    and  account_id not in (select account_id from streams where year(stream_date) = 2021)