'''https://leetcode.com/problems/search-insert-position/'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while hi >= lo:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

