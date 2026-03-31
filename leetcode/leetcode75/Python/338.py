#https://leetcode.com/problems/counting-bits/description/

#Using 191 problem. Hamming weight
class Solution:
    def countBits(self, n: int) -> List[int]:
        def return_count(number):
            bits = 0
            while number != 0:
                bits += 1
                number = number & (number - 1)
            return bits
        result = []
        for i in range(n + 1):
            result.append(return_count(i))
        return result
