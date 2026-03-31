#https://leetcode.com/problems/unique-number-of-occurrences/description/


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt_dict = {}
        for i in arr:
            if i in cnt_dict:
                cnt_dict[i] += 1
            else:
                cnt_dict[i] = 1
        u_dict = {}
        for k, v in cnt_dict.items():
            if v in u_dict:
                return False
            else:
                u_dict[v] = 1
        return True