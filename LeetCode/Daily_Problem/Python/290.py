#https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        map_dict = {}
        ptr = 0
        if len(pattern) != len(words):
            return False
        for i in pattern:
            if (i in map_dict and words[ptr]):
                if map_dict[i] == words[ptr]:
                    ptr += 1
                else:
                    return False
            elif (i not in map_dict and words[ptr] in map_dict.values()):
                return False
            else:
                map_dict[i] = words[ptr]
                ptr += 1
        return True