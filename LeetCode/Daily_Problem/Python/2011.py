#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            ops = i.replace('X','')
            if ops == '++':
                x += 1
            else:
                x -=1
        return x