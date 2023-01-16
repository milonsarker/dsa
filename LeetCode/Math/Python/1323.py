#https://leetcode.com/problems/maximum-69-number/description/


class Solution:
    def maximum69Number (self, num: int) -> int:
        strnum = list(str(num))
        for i in range(len(strnum)):
            if int(strnum[i]) == 6:
                strnum[i] = '9'
                break
        return int(''.join(strnum))