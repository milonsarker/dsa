'''https://leetcode.com/problems/replace-elements-in-an-array/'''

'''Time Limit Exceed'''
class Solution:
    def search(self, nums, target):
        l , r = 0, len(nums) -1
        while r >= l:
            if nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            else:
                l += 1
                r -= 1
        return -1
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        k = len(operations) -1
        if len(nums) == 1:
            return [operations[k][1]]
        for i in range(len(operations)):
            target = operations[i][0]
            index = self.search(nums,target)
            if index != -1:
                nums[index] = operations[i][1]
        return nums

'''Accepted Solution: Used Dictionary for Index identification'''

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_dic = {num: i for i, num in enumerate(nums)}

        for f, s in operations:
            idx = num_dic[f]
            nums[idx] = s
            num_dic[s] = idx
            del num_dic[f]
        return nums

''' Best Method:  Swap mapping'''
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        swaps = {}
        for s, e in reversed(operations):
            swaps[s] = swaps[e] if e in swaps else e
        print(swaps)
        for i, num in enumerate(nums):
            if num in swaps:
                nums[i] = swaps[num]
        return nums