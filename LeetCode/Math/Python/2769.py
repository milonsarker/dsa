#https://leetcode.com/problems/find-the-maximum-achievable-number/
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t * 2)