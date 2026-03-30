#https://leetcode.com/problems/product-of-array-except-self/description/

#Solution with O(n) complexity and O(n) space complexity

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pre_arr = [0] * len(nums)
        suff_arr = [0] * len(nums)
        pre_arr[0] = 1
        suff_arr[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            pre_arr[i] = nums[i - 1] * pre_arr[i - 1]

        for i in reversed(range(len(nums) - 1)):
            suff_arr[i] = nums[i + 1] * suff_arr[i + 1]

        for i in range(len(nums)):
            ans[i] = pre_arr[i] * suff_arr[i]

        return ans


#Solution with O(n) Complexity and O(1) Complexity

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        suff = 1
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i -1]
        for i in reversed(range(len(nums))):
            ans[i] = ans[i] * suff
            suff *= nums[i]
        return ans