#https://leetcode.com/problems/number-of-1-bits/description/

#Optimal Soluton
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n != 0:
            bits += 1
            n = n & (n - 1)
        return bits;