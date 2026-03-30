#https://leetcode.com/problems/calculate-money-in-leetcode-bank/

#Method : Looping
#Time Complexity : O(n)
#Space Complexity : O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        pre_mon = 0
        total = 0
        pre_val = 0

        for i in range(n):
            rem = i % 7
            if rem == 0:
                pre_mon += 1
                total += pre_mon
                pre_val = pre_mon
            else:
                pre_val += 1
                total += pre_val
        return total

#Method : Mathematical
#Tiem Complexity : O(1)
#Space Complexity : O(1)
		
class Solution:
    def totalMoney(self, n: int) -> int:
        F = 28
        K = n // 7
        rem = n % 7 
        L = 28 + (K - 1) * 7
        total = (K * (F + L) / 2)
        lw = K
        for i in range(rem):
            lw += 1
            total += lw
        return int(total)