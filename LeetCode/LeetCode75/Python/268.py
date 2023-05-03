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

#Bit Manipulation; Complexity = O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = len(nums)
        for i, num in enumerate(nums):
            missing_number = missing_number ^ i ^ num
        return missing_number

#Gauss Formula; Complexity = O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        gauss_val = n * (n + 1)/2
        nums_sum = sum(nums)
        return round(gauss_val - nums_sum)