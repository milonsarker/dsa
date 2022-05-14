#https://leetcode.com/contest/biweekly-contest-78/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        snum = str(num)
        cnt = 0
        while len(snum) >= k:
            div = int(snum[:k])
            if div != 0 and num % div == 0:
                cnt += 1
            snum = snum[1:]
        return cnt