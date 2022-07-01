'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10 ** 4
        maxProfit = 0
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit