#https://leetcode.com/problems/maximum-subarray/

#Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_subarr  = max_subarr = nums[0]
        for n in nums[1:]:
            curr_subarr = max(n, curr_subarr + n)
            max_subarr = max(curr_subarr, max_subarr)
        return max_subarr