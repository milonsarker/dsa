#https://leetcode.com/problems/single-number/description/

#bit manipulation : complexity : O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        return result