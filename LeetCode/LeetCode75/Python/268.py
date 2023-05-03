#https://leetcode.com/problems/missing-number/description/

#from top of my head. Using loop

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_dict = {}
        for i in range(n):
            if i not in nums:
                return i
        return i + 1

