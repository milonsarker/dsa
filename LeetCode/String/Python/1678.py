#https://leetcode.com/problems/goal-parser-interpretation/description/


#From top of my head
class Solution:
    def interpret(self, command: str) -> str:
        cMap = {"()": 'o', 'G':'G',"(al)":"al"}
        stack = []
        result = []
        for char in command:
            if char in cMap:
                result.append(cMap[char])
            else:
                stack.append(char)
            sComm = ''.join(stack)
            if  sComm in cMap:
                result.append(cMap[sComm])
                stack = []
        return ''.join(result)

