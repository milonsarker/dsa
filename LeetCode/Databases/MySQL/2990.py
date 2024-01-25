--https://leetcode.com/problems/loan-types/

select distinct a.user_id 
    from loans a 
    join loans b
    on (a.user_id = b.user_id)
    where a.loan_type = 'Mortgage' and b.loan_type = 'Refinance'
    order by 1 ;