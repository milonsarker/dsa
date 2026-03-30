#__https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m  = len(mat)
        n = len(mat[0])
        one_d = []
        ret_mat = []
        if m * n !=  r * c:
            return mat
        for i in range(m):
            for j in range(n):
                one_d.append(mat[i][j])
        length_one_d = len(one_d)
        iterator = 0
        for i in range(r):
            ret_mat.append([])
            for j in range(c):
                ret_mat[i].append(one_d[iterator])
                iterator += 1


        return ret_mat