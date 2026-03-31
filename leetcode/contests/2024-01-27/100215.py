class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnter = 0
        sLen = len(s)
        if sLen <= 1:
            return 0
        pointer = s[0]
        for i in range(1, sLen):
            cmp_char = s[i]
            if pointer.lower() == cmp_char.lower():
                continue
            else: 
                cnter += 1
            pointer = cmp_char
        return cnter