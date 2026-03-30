'''https://leetcode.com/problems/pascals-triangle/'''

'''Dynamic Problem'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        pre_row = []
        for i in range(1,numRows + 1):
            cur_row = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    cur_row.append(1)
                else:
                    cur_row.append(pre_row[j-1] + pre_row[j])
            result.append(cur_row)
            pre_row = cur_row
        return result