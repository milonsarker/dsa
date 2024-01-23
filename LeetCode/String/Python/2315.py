#https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        pairFlag = False
        ccnt = 0
        for i in range(len(s)):
            if s[i] == '|' and not pairFlag:
                pairFlag = True
            elif s[i] == '|' and pairFlag:
                pairFlag = False
            if not pairFlag and s[i] == '*':
                ccnt += 1
        return ccnt