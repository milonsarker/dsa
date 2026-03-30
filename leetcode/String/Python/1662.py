#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for a, b in zip(self.generate(word1), self.generate(word2)):
            if a != b:
                return False
        return True
        

    def generate(self, wordlist: List[str]):
        for word in wordlist:
            for ch in word:
                yield ch
        yield None