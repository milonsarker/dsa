#https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sofar = nums[0]
        min_sofar = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max_sofar  = max(curr, max_sofar * curr, min_sofar * curr)
            min_sofar  = min(curr, max_sofar * curr, min_sofar * curr)
            max_sofar = temp_max_sofar
            result = max(result, max_sofar)
        return result