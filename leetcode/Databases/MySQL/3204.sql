#https://leetcode.com/problems/bitwise-user-permissions-analysis/

# Write your MySQL query statement below
select bit_and(permissions) common_perms, bit_or(permissions) any_perms
    from user_permissions
    ;