#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen = len(haystack)
        nlen = len(needle)
        for window_start in range(hlen - nlen + 1):
            for i in range(nlen):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == nlen -1:
                    return window_start
        return -1
        