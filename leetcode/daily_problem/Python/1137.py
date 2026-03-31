#https://leetcode.com/problems/n-th-tribonacci-number/

#learn


class Tri:
    def __init__(self):
        def helper(k):
            if k == 0:
                return 0

            if nums[k]:
                return nums[k]

            nums[k] = helper(k - 1) + helper(k - 2) + helper(k - 3)
            return nums[k]

        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        helper(n - 1)


class Solution:
    t = Tri()

    def tribonacci(self, n: int) -> int:
        return self.t.nums[n]