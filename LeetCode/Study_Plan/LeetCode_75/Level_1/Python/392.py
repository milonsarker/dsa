'''https://leetcode.com/problems/is-subsequence/'''


'''Solution: Out of my head
Method : Two pointer'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl = list(s)
        if len(sl) == 0:
            return True
        ind = 0
        for i in list(t):
            if i == sl[ind]:
                ind += 1
            if ind == len(sl):
                return True
        return False