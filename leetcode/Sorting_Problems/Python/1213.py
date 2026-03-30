#https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        reList = list(set(arr1) & set(arr2) & set(arr3))
        reList.sort()
        return reList


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1, p2, p3 = 0, 0, 0
        lenArr1, lenArr2, lenArr3 = len(arr1), len(arr2), len(arr3)
        result = []
        while p1 < lenArr1 and p2 < lenArr2 and p3 < lenArr3:
            if arr1[p1] == arr2[p2] and arr2[p2] == arr3[p3]:
                result.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1
        return result
