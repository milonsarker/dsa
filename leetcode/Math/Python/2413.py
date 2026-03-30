#https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        k = n 
        while True: 
            if k % 2 == 0 and k % n ==0:
                return k
            else:
                k += 1
        
#https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 2 if n % 2 else n