#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in sentences:
            sLen = len(i.split(' '))
            ans = max(sLen, ans)
        return ans