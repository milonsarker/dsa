#https://leetcode.com/problems/xor-operation-in-an-array/description/

#O(n)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = None
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
            if i == 0:
                result = start + 2 * i
            elif i >= 1:
                result = result ^ (start + 2 * i)
        return result