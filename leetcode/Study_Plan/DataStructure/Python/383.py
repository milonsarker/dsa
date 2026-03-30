#https://leetcode.com/problems/ransom-note/description/?envType=study-plan&id=data-structure-i

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_dict = {}
        for i in magazine:
            if i in cnt_dict:
                cnt_dict[i] += 1
            else:
                cnt_dict[i] = 1
        for i in ransomNote:
            if i in cnt_dict and cnt_dict[i] > 0:
                cnt_dict[i] -= 1
            else:
                return False
        return True
