#https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan&id=data-structure-i

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        data = []
        for row in matrix:
            data.extend(row)
        left = 0
        right = len(data) -1
        print(data)
        while right >= left:
            mid = (left + right) // 2
            if data[mid] == target:
                return True
            elif target > data[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False