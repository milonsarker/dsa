#https://leetcode.com/problems/confusing-number/description/

class Solution:
    def confusingNumber(self, n: int) -> bool:

        if n == 0:
            return False
        s_num = str(n)
        c_num = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        ro_num = []
        for i in s_num:
            if i in c_num:
                ro_num.append(c_num[i])
            else:
                return False
        if int(''.join(ro_num[::-1])) == n:
            return False
        else:
            return True