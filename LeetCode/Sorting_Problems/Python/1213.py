#https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        reList = list(set(arr1) & set(arr2) & set(arr3))
        reList.sort()
        return reList