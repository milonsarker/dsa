'''https://leetcode.com/problems/move-zeroes/'''

'''Brute Force : Time Limit Exceed Error'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(n-i - 1):
                if nums[j] == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

'''Brute Force: Accepted but very time consuming'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i] ==0:
                for j in range(i + 1, n):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
'''Optimal Solution'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lastNonZeroAt = 0
        for i in range(n):
            if nums[i] != 0:
                nums[lastNonZeroAt], nums[i] = nums[i], nums[lastNonZeroAt]
                lastNonZeroAt += 1
