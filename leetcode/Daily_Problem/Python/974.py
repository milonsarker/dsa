#https://leetcode.com/problems/subarray-sums-divisible-by-k/description/


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefixMod, result = 0, 0

        modGroups = [0] * k
        modGroups[0] = 1

        for num in nums:
            prefixMod = (prefixMod + num) % k
            result += modGroups[prefixMod]
            modGroups[prefixMod] += 1

        return result