#https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        diff_dict = {}
        for i in tasks:
            if i in diff_dict:
                diff_dict[i] += 1
            else:
                diff_dict[i] = 1

        cntr = 0
        for key, val in diff_dict.items():
            quotient = val // 3
            remainder = val % 3
            if val == 1:
                return -1
            elif val % 3 == 0:
                cntr += val / 3
            else:
                cntr += val // 3 + 1
        return int(cntr)