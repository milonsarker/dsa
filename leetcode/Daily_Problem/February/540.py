#https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        prev = nums[0]
        cnt = 0
        lngth = len(nums) - 1
        if lngth == 0:
            return nums[0]
        while True:
            if cnt + 1 <= lngth:
                if nums[cnt] == nums[cnt + 1]:
                    cnt += 2
                else:
                    return nums[cnt]
            else:
                return nums[cnt]
        return 0