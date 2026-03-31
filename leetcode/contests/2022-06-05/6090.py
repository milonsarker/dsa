'''https://leetcode.com/contest/weekly-contest-296/problems/min-max-game/'''

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n >= 1:
            if n == 1:
                return nums[0]
            newNums = [0] * (n//2)
            for i in range(n):
                if i % 2 == 0 and (0 <= i and i < n / 2):
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
                elif i % 2 != 0 and (0 <= i and i < n / 2):
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = newNums
            n = len(nums)
            print(nums)

