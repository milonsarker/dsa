#https://leetcode.com/problems/delete-columns-to-make-sorted/


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs_list = [list(i) for i in strs]
        ctnr = 0
        for i in range(len(strs_list[0])):
            temp = [strs_list[j][i] for j in range(len(strs_list))]
            if ''.join(temp) != ''.join(sorted(temp)):
                ctnr += 1
        return ctnr
