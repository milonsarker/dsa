#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

class Solution:
    def selection_sort(self, idata):
        sorted_data = []
        while len(idata) > 0:
            minimum = 0
            for i in range(len(idata)):
                if idata[i][1] <= idata[minimum][1]:
                    minimum = i
            sorted_data.append(idata.pop(minimum))
        return sorted_data

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorted_points = self.selection_sort(points)
        points.sort(key=lambda x: x[1])
        min_cntr = 0
        start = 0
        print(points)
        for i in points:
            if start != 0:
                if start[1] >= i[0]:
                    continue
                else:
                    min_cntr += 1
                    start = i
            else:
                start = i
                min_cntr += 1
        return min_cntr