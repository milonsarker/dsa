'''https://leetcode.com/problems/reverse-words-in-a-string-iii/'''

'''Algorithm: Two Pointer'''

class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        for word in s.split():
            l, r = 0, len(word) - 1
            word = list(word)
            while r > l:
                word[l], word[r] = word[r], word[l]
                l, r = l + 1, r - 1
            output.append(''.join(word))
        return ' '.join(output)