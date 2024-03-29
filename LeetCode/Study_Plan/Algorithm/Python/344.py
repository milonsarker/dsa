'''https://leetcode.com/problems/reverse-string/'''

'''Algorithm: Two Pointer; Time Complexity: O(n)'''

class Solution:
    def reverseString(self,s: List[str]) -> None:
        left = 0
        right = len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right -1