#https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan&id=data-structure-i

class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i not in pair:
                stack.append(i)
            else:
                if len(stack) != 0:
                    check = stack.pop()
                else:
                    return False
                if check != pair[i]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

