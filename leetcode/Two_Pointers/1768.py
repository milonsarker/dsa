#https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        flen = len(word1)
        slen = len(word2)
        ldiff = flen - slen
        result = ''
        i = 0
        for i in range(min(flen, slen)):
            result = result + word1[i] + word2[i]
        if ldiff > 0:
            result = result + word1[i+1:]
        else:
            result = result + word2[i+1:]
        return result