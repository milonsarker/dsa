'''https://leetcode.com/problems/two-sum/'''

'''Using Hashing Technique'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preVal = {}
        for index , data in enumerate(nums):
            diff = target - data
            if diff in preVal:
                return [preVal[diff],index]
            preVal[data] = index
        return -1