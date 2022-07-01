'''https://leetcode.com/problems/find-pivot-index/'''

'''Out of my head solution'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = total
        for i, n in enumerate(nums):
            if i == 0:
                right -= nums[i]
                if left == right:
                    return i
            else:
                left += nums[i - 1]
                right -= nums[i]
                if left == right:
                    return i
        return -1
