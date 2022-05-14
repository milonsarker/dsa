from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        tot = sum(nums)
        cnt = 0
        fpart = 0
        for i in range(len(nums) - 1):
            fpart += nums[i]
            lpart = tot - fpart
            if fpart >= lpart:
                cnt += 1
        return cnt

if __name__=="__main__":
    data = [10,4,-8,7]
    sobj = Solution()
    output = sobj.waysToSplitArray(data)
    print(output)