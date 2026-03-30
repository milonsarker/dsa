#https://leetcode.com/problems/max-points-on-a-line/description/


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for  i in range(n):
            pdict = {}
            for j in range(n):
                if i != j:
                    tval = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
                    if tval in pdict:
                        pdict[tval] += 1
                    else:
                        pdict[tval] = 1
            result = max(result, max(pdict.values()) + 1)
        return result