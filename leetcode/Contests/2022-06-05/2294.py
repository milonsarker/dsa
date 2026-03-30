'''https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/'''

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        start = nums[0]
        for item in nums:
            diff = item - start
            if diff > k:
                ans += 1
                start = item
        return ans