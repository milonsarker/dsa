#https://leetcode.com/problems/maximum-ice-cream-bars/description/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cntr = 0
        for i in costs:
            if i <= coins:
                cntr += 1
                coins -= i
            else:
                break
        return cntr