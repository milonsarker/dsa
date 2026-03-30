##___-https://leetcode.com/contest/weekly-contest-293/problems/maximum-consecutive-floors-without-special-floors/

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        left = bottom
        special.sort()
        highest = 0
        n = len(special)
        for i in range(n):
            if i != n-1:
                floor_cnt = special[i] - left
                if floor_cnt > highest:
                    highest = floor_cnt
                left = special[i]+1
            elif i == n-1:
                floor_cnt = special[i] -left
                if floor_cnt > highest:
                    highest = floor_cnt
                floor_cnt = top - special[i]
                if floor_cnt > highest:
                    highest = floor_cnt
        return highest