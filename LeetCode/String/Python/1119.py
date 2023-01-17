#https://leetcode.com/problems/remove-vowels-from-a-string/description/


import re
class Solution:
    def removeVowels(self, s: str) -> str:
        vo = ['a', 'e', 'i', 'o', 'u']
        vregex = re.compile('|'.join(map(re.escape, vo)))
        output = vregex.sub("", s)
        return output