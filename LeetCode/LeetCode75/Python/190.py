#https://leetcode.com/problems/reverse-bits/submissions/


#Bit Manipulation
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            temp = (n>>i) & 1
            if temp:
                result = result | (temp << (31-i))
        return result