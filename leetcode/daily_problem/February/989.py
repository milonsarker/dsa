#https://leetcode.com/problems/add-to-array-form-of-integer/description/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = (''.join(map(str, num)))
        fin = int(result) + k
        return map(int, list(str(fin)))