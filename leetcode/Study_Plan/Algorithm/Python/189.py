'''https://leetcode.com/problems/rotate-array/'''


'''Time Limit Exceeded'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = -1
            pre = -1
            for x in range(len(nums)):
                if x == 0:
                    temp = nums[x]
                    nums[x] = nums[len(nums) - 1]
                    pre = temp
                else:
                    temp = nums[x]
                    nums[x] = pre
                    pre = temp

'''Using Extra Array'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        nums[:] = a