'''https://leetcode.com/problems/squares-of-a-sorted-array/'''

'''Two pointer alogorithm used'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        n = len(nums)

        result = []

        while n > 0:
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2
            if left_squared >= right_squared:
                result.insert(0, left_squared)
                left += 1
            else:
                result.insert(0, right_squared)
                right -= 1
            n -= 1
        return result