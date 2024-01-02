--https://leetcode.com/problems/account-balance/

/* Write your PL/SQL query statement below */
select account_id, to_char(day) day,
        sum(
                case when type = 'Deposit' then 1 else -1 end * amount
           ) over (partition by account_id order by day asc) balance
    from transactions
    order by 1, 2;