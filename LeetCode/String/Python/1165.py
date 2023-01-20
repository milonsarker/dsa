#https://leetcode.com/problems/single-row-keyboard/description/

#From top of my head
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        k = list(keyboard)
        keystroke = 0
        pos = 0
        for i in word:
            keystroke += abs(k.index(i) - pos)
            pos = k.index(i)
        return keystroke