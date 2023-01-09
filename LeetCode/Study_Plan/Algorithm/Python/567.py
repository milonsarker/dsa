#https://leetcode.com/study-plan/algorithm/?progress=xl0ohgkv


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sdic = {}
        for i in s1:
            if i in sdic:
                sdic[i] += 1
            else:
                sdic[i] = 1
        cpy = dict(sdic)
        for j in range(len(s2) - len(s1) + 1):
            cpy = dict(sdic)
            for i in s2[j: j + len(s1)]:
                    if i in cpy:
                        if cpy[i] == 1:
                            cpy.pop(i)
                        else:
                            cpy[i] -= 1
            if bool(cpy) == False:
                return True
        return False
