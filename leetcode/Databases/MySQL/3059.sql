#https://leetcode.com/problems/find-all-unique-email-domains/
# Write your MySQL query statement below

select substring(email, instr(email, '@') + 1) email_domain, count(*) count   
    from emails
    where email like '%com'
    group by substring(email, instr(email, '@') + 1)
    order by substring(email, instr(email, '@') + 1)
    ;