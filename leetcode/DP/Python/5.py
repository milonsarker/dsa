#https://leetcode.com/problems/longest-palindromic-substring/description/


#Learn

#This is a solution by chatgpt
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(longest) >= j - i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    longest = s[i:j]
                    break
        return longest

