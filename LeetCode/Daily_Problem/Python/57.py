#https://leetcode.com/problems/insert-interval/description/


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        x, y = newInterval[0], newInterval[1]
        for i in intervals:
            m = i[0]
            n = i[1]
            if n < x:
                result.append(i)
            elif m > y:
                result.append([x, y])
                x = m
                y = n
            elif n >= x or m <= y:
                x = min(m, x)
                y = max(n, y)
        result.append([x, y])
        return result



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        x, y = newInterval[0], newInterval[1]
        for i in range(len(intervals)):
            m = intervals[i][0]
            n = intervals[i][1]
            if n < x:
                result.append(intervals[i])
            elif m > y:
                result.append([x,y])
                result.extend(intervals[i:])
                return result
            elif n >= x or m <= y:
                x = min(m, x)
                y = max(n, y)
        result.append([x,y])
        return result